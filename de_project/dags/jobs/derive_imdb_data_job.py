"""Job codes for derive imdb data DAG"""
import io
from os import environ
import pandas as pd
import psycopg2
from pyspark.sql import SparkSession

from manage_buckets import get_s3_connection


def get_spark_session() -> SparkSession:
    """Function create and return spark session"""
    spark = (SparkSession.builder
             .master('local[*]')
             .appName('task1')
             .getOrCreate())
    return spark


def get_imdb_ratings_dataframe(s3_connection, bucket_name, file_name):
    """Function that get and return film's ratings dataframe"""
    file_object = s3_connection.Bucket(bucket_name).Object(file_name).get()['Body'].read()
    dataframe = pd.read_csv(io.BytesIO(file_object), delimiter="\t", low_memory=False)
    return dataframe


def update_ratings_in_db(ratings_df):
    """Function that update films table by ratings"""
    conn = psycopg2.connect("dbname='films' user='airflow' host='database' password='airflow'")
    cur = conn.cursor()

    rows = zip(ratings_df.tconst, ratings_df.averageRating, ratings_df.numVotes)
    cur.execute("""CREATE TEMP TABLE ratings(tconst VARCHAR,
                                             averageRating INTEGER,
                                             numVotes INTEGER) ON COMMIT DROP""")
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
    update_ratings_in_db(ratings_dataframe)
