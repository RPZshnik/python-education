"""Job codes for load data to postgres DAG"""
from os import environ

import boto3
from botocore.config import Config
from pyspark.shell import sc
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import posexplode, col, lit
from pyspark.sql import types
from pyspark.sql.types import IntegerType, DoubleType
from sqlalchemy import create_engine

schema = types.StructType(fields=[
    types.StructField("adult", types.BooleanType()),
    types.StructField("backdrop_path", types.StringType()),
    types.StructField("belongs_to_collection", types.StringType()),
    types.StructField("budget", types.LongType()),
    types.StructField("genres",
                      types.ArrayType
                      (types.StructType(fields=[types.StructField("id",
                                                                  types.LongType()),
                                                types.StructField("name",
                                                                  types.StringType())]))),
    types.StructField("homepage", types.StringType()),
    types.StructField("id", types.LongType()),
    types.StructField("imdb_id", types.StringType()),
    types.StructField("original_language", types.StringType()),
    types.StructField("original_title", types.StringType()),
    types.StructField("overview", types.StringType()),
    types.StructField("popularity", types.DoubleType()),
    types.StructField("poster_path", types.StringType()),
    types.StructField("production_companies", types.StringType()),
    types.StructField("production_countries", types.StringType()),
    types.StructField("release_date", types.StringType()),
    types.StructField("revenue", types.IntegerType()),
    types.StructField("runtime", types.IntegerType()),
    types.StructField("spoken_languages", types.StringType()),
    types.StructField("status", types.StringType()),
    types.StructField("tagline", types.StringType()),
    types.StructField("title", types.StringType()),
    types.StructField("video", types.BooleanType()),
    types.StructField("vote_average", types.DoubleType()),
    types.StructField("vote_count", types.IntegerType())
])


def get_s3_connection():
    """Function create and return s3 connection"""
    user = environ.get('MINIO_ROOT_USER')
    password = environ.get('MINIO_ROOT_PASSWORD')
    session = boto3.session.Session()
    s3_connection = session.resource(
        's3',
        endpoint_url='http://s3:9000',
        aws_access_key_id=user,
        aws_secret_access_key=password,
        config=Config(signature_version='s3v4'),
        region_name='us-west-1'
    )
    return s3_connection


def get_db_connection(db_name=None):
    """Function create and return db connection"""
    db_user = environ.get("POSTGRES_USER")
    db_port = environ.get("POSTGRES_PORT")
    db_password = environ.get('POSTGRES_PASSWORD')
    if db_name is None:
        db_connection = create_engine(f'postgresql+psycopg2://{db_user}:'
                                      f'{db_password}@database:{db_port}')
    else:
        db_connection = create_engine(f'postgresql+psycopg2://{db_user}:'
                                      f'{db_password}@database:{db_port}/{db_name}')
    return db_connection


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = (SparkSession.builder
             .master('local[4]')
             .config("spark.executor.memory", "70g")
             .config("spark.driver.memory", "50g")
             .config("spark.memory.offHeap.enabled", True)
             .config("spark.memory.offHeap.size", "16g")
             .appName('task1')
             .getOrCreate())
    return spark


def __get_data_files(s3_connection, bucket_name):
    """Function return json files"""
    json_files = []
    bucket = s3_connection.Bucket(bucket_name)
    for file_object in bucket.objects.all():
        json_files.append(file_object.get()['Body'].read().decode('utf-8'))
    return json_files


def __get_dataframe_from_data_files(spark, data_files):
    if len(data_files) < 1:
        return None

    dataframe = spark.read.schema(schema).json(sc.parallelize([data_files[0]]))
    for data_file in data_files[1:]:
        dataframe = dataframe.union(spark.read.schema(schema)
                                    .json(sc.parallelize([data_file])))

    return dataframe


def __transform_dataframe(dataframe: DataFrame) -> DataFrame:
    dataframe = (dataframe.select("id", "imdb_id", "adult", "original_language",
                                  "original_title", "popularity", "release_date",
                                  "runtime", "status", posexplode("genres").
                                  alias("pos", "genre")).where(col("pos") < 1))
    dataframe = dataframe.select("id", "imdb_id", "adult", "original_language",
                                 "original_title", "popularity", "release_date",
                                 "runtime", "status", col("genre.name").alias("genre"))
    dataframe = (dataframe
                 .withColumn("average_rating", lit(0).cast(DoubleType()))
                 .withColumn("num_votes", lit(0).cast(IntegerType())))
    return dataframe


def __save_dataframe_to_db(db_connection, dataframe: DataFrame):
    dataframe.toPandas().to_sql('films', db_connection,
                                index=False, if_exists='append')
    del dataframe


def load_data_to_postgres():
    """Function that implement parse and save data to minio"""
    db_name = environ.get("FILMS_POSTGRES_TABLE_NAME")
    s3_connection = get_s3_connection()
    db_connection = get_db_connection(db_name)
    spark = get_spark_session()
    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    data_files = __get_data_files(s3_connection, bucket_name)
    for index in range(0, len(data_files), 100):
        dataframe = __get_dataframe_from_data_files(spark, data_files[index:index+100])
        dataframe = __transform_dataframe(dataframe)
        dataframe.show()
        __save_dataframe_to_db(db_connection, dataframe)
