"""Job codes for derive imdb data DAG"""
import io
from os import environ
import pandas as pd
import boto3
import psycopg2
from botocore.config import Config
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import posexplode, col, lit
from sqlalchemy import create_engine


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


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = (SparkSession.builder
             .master('local[*]')
             .appName('task1')
             .getOrCreate())
    return spark


def get_imdb_ratings_dataframe(s3_connection, bucket_name, file_name):
    spark = get_spark_session()
    file_object = s3_connection.Bucket(bucket_name).Object(file_name).get()['Body'].read()
    dataframe = pd.read_csv(io.BytesIO(file_object), delimiter="\t", low_memory=False)
    # dataframe = spark.createDataFrame(dataframe)
    return dataframe


def update_ratings_in_db(ratings_df):
    conn = psycopg2.connect("dbname='films' user='airflow' host='database' password='airflow'")
    cur = conn.cursor()

    rows = zip(ratings_df.tconst, ratings_df.averageRating, ratings_df.numVotes)
    cur.execute("""CREATE TEMP TABLE ratings(tconst VARCHAR, averageRating INTEGER, numVotes INTEGER) ON COMMIT DROP""")
    cur.executemany("""INSERT INTO ratings(tconst, averageRating, numVotes) 
                        VALUES(%s, %s, %s)""", rows)

    cur.execute("""
        UPDATE
            films
        SET 
            average_rating = ratings.averageRating,
            num_votes = ratings.numVotes
        FROM 
            ratings
        WHERE 
            ratings.tconst = films.imdb_id;
        """)

    conn.commit()
    cur.close()
    conn.close()


def derive_imdb_data():
    """Function that implement parse and save data to minio"""
    s3_connection = get_s3_connection()
    bucket_name = environ.get("MINIO_IMDB_DATA_BUCKET_NAME")
    ratings_dataframe = get_imdb_ratings_dataframe(s3_connection, bucket_name, "title.ratings.tsv")
    print(ratings_dataframe)
    print(ratings_dataframe.info)
    update_ratings_in_db(ratings_dataframe)
