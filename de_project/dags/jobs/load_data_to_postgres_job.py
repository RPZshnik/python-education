"""Job codes for update movies DAG"""
import concurrent.futures
import time
from os import environ
from datetime import datetime, timedelta
import json
import boto3
import requests
from botocore.config import Config
from pyspark.shell import sc
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType, LongType, DoubleType, \
    ArrayType
from requests.exceptions import RequestException
from sqlalchemy import create_engine

schema = StructType(fields=[
    StructField("adult", BooleanType()),
    StructField("backdrop_path", StringType()),
    StructField("belongs_to_collection", StringType()),
    StructField("budget", LongType()),
    StructField("genres",
                ArrayType(StructType(fields=[StructField("id", LongType()), StructField("name", StringType())]))),
    StructField("homepage", StringType()),
    StructField("id", LongType()),
    StructField("imdb_id", StringType()),
    StructField("original_language", StringType()),
    StructField("original_title", StringType()),
    StructField("overview", StringType()),
    StructField("popularity", DoubleType()),
    StructField("poster_path", StringType()),
    StructField("production_companies", StringType()),
    StructField("production_countries", StringType()),
    StructField("release_date", StringType()),
    StructField("revenue", IntegerType()),
    StructField("runtime", IntegerType()),
    StructField("spoken_languages", StringType()),
    StructField("status", StringType()),
    StructField("tagline", StringType()),
    StructField("title", StringType()),
    StructField("video", BooleanType()),
    StructField("vote_average", DoubleType()),
    StructField("vote_count", IntegerType())
])


def __get_s3_connection():
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


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = (SparkSession.builder
             .master('local[*]')
             .appName('task1')
             .getOrCreate())
    return spark


def get_db_connection():
    db_user = environ.get("POSTGRES_USER")
    db_port = environ.get("POSTGRES_PORT")
    db_password = environ.get('POSTGRES_PASSWORD')
    db_connection = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@database:{db_port}/films')
    return db_connection


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
        df = spark.read.schema(schema).json(sc.parallelize([data_file]))
        dataframe = dataframe.union(df)

    return dataframe


def __transform_dataframe(dataframe):
    dataframe = dataframe.select("id", "imdb_id", "adult", "original_language",
                                 "original_title", "popularity", "release_date",
                                 "runtime", "status")
    return dataframe


def __save_dataframe_to_db(db_connection, dataframe: DataFrame):
    dataframe.toPandas().to_sql('films', db_connection,
                                index=False, if_exists='append')


def load_data_to_postgres():
    """Function that implement parse and save data to minio"""
    s3_connection = __get_s3_connection()
    spark = get_spark_session()
    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    data_files = __get_data_files(s3_connection, bucket_name)
    dataframe = __get_dataframe_from_data_files(spark, data_files)
    if dataframe is None:
        return
    dataframe = __transform_dataframe(dataframe)
    db_connection = get_db_connection()
    __save_dataframe_to_db(db_connection, dataframe)
