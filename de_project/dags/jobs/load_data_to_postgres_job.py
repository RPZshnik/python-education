"""Job codes for load data to postgres DAG"""
from os import environ
from pyspark.shell import sc
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import posexplode, col, lit
from pyspark.sql.types import IntegerType, DoubleType

from manage_postgres import get_db_connection
from manage_buckets import get_s3_connection
from schemas import tmdb_schema


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

    dataframe = spark.read.schema(tmdb_schema).json(sc.parallelize([data_files[0]]))
    for data_file in data_files[1:]:
        dataframe = dataframe.union(spark.read.schema(tmdb_schema)
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
    dataframe = dataframe.withColumn("average_rating",
                                     (lit(None).cast(DoubleType()))
                                     .withColumn("num_votes", lit(0).cast(IntegerType())))
    return dataframe


def __save_dataframe_to_db(db_connection, dataframe: DataFrame):
    dataframe.toPandas().to_sql('films', db_connection,
                                index=False, if_exists='append')
    del dataframe


def load_data_to_postgres():
    """Function that implement parse and save data to minio"""
    s3_connection = get_s3_connection()
    db_connection = get_db_connection()
    spark = get_spark_session()
    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    data_files = __get_data_files(s3_connection, bucket_name)
    for index in range(0, len(data_files), 100):
        dataframe = __get_dataframe_from_data_files(spark, data_files[index:index+100])
        dataframe = __transform_dataframe(dataframe)
        __save_dataframe_to_db(db_connection, dataframe)
