"""Job code for transform and save to parquet DAG"""
import io
from os import environ
from datetime import datetime

import boto3
from botocore.config import Config

from pyspark.sql import functions as f
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import to_timestamp, from_unixtime, col

exchangers_json_schemas = {'bitfinex': {"exchanger_name": "bitfinex",
                                        "time": {"time_field": "timestamp",
                                                 "time_format": "unix_time"},
                                        "ttype_field": "type",
                                        "amount_field": "amount",
                                        "price_field": "price"
                                        },
                           'bitmex': {"exchanger_name": "bitmex",
                                      "time": {"time_field": "timestamp",
                                               "time_format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"},
                                      "ttype_field": "side",
                                      "amount_field": "homeNotional",
                                      "price_field": "price"},
                           'poloniex': {"exchanger_name": "bitfinex",
                                        "time": {"time_field": "date",
                                                 "time_format": "yyyy-MM-dd HH:mm:ss"},
                                        "ttype_field": "type",
                                        "amount_field": "amount",
                                        "price_field": "rate"}}


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
             .appName('task')
             .getOrCreate())
    return spark


def get_json_file_keys(bucket):
    """Function return bucket files names"""
    keys = []
    for obj in bucket.objects.all():
        keys.append(obj.key)
    return keys


def get_json_file(s3_connection, bucket, file_name):
    """Function return json file by bucket name"""
    content_object = s3_connection.Object(bucket, file_name)
    json_file = content_object.get()['Body'].read().decode('utf-8')
    return json_file


def get_dataframe_from_json(spark: SparkSession, json_file) -> DataFrame:
    """Function read and return dataframe from json"""
    sc = spark.sparkContext
    dataframe = spark.read.json(sc.parallelize([json_file]))
    return dataframe


def get_dataframe_from_json_files(spark: SparkSession, s3_connection, bucket: str, keys: list):
    """Function return concatenated dataframe from json files"""
    if len(keys) < 1:
        return None

    json_file = get_json_file(s3_connection, bucket, keys[0])
    dataframe = get_dataframe_from_json(spark, json_file)
    for file_key in keys[1:]:
        json_file = get_json_file(s3_connection, bucket, file_key)
        dataframe = dataframe.union(get_dataframe_from_json(spark, json_file))
    return dataframe


def convert_date(dataframe: DataFrame, time_field: str, time_format=None) -> DataFrame:
    """Function convert date to correct format"""
    dateformat = "MM-dd-yyyy HH:mm:ss"
    if time_format == "unix_time":
        dataframe = dataframe.withColumn("transaction_time",
                                         from_unixtime(col(time_field), dateformat))
    else:
        dataframe = dataframe.withColumn("transaction_time",
                                         to_timestamp("transaction_time", time_format))
    return dataframe


def rename_columns(dataframe, json_schema):
    """Function rename columns in dataframe"""
    time_field = json_schema["time"]["time_field"]
    transaction_type = json_schema["ttype_field"]
    amount_field = json_schema["amount_field"]
    price_field = json_schema["price_field"]
    prev_names = [time_field, transaction_type, amount_field, price_field]
    new_names = ["transaction_time", "type", "amount", "price"]
    for prev_name, new_name in zip(prev_names, new_names):
        dataframe = dataframe.withColumnRenamed(prev_name, new_name)
    return dataframe


def transform_dataframe(dataframe: DataFrame, exchanger_name: str) -> DataFrame:
    """Function transform dataframe"""
    json_schema = exchangers_json_schemas[exchanger_name]
    dataframe = rename_columns(dataframe, json_schema)
    dataframe = dataframe.withColumn("exchanger", f.lit(json_schema["exchanger_name"]))
    dataframe = convert_date(dataframe, "transaction_time",
                             json_schema["time"]["time_format"])
    dataframe = dataframe.select("exchanger", "transaction_time", "type", "amount", "price")
    return dataframe


def save_dataframe_to_parquet(dataframe: DataFrame, s3_connection, bucket: str):
    """Function save dataframe to parquet in bucket"""
    bucket_name = f"{bucket}-parquet"
    with io.BytesIO() as buffer:
        dataframe.toPandas().to_parquet(buffer, index=False)
        date_time = datetime.now()
        s3_connection.Bucket(bucket_name).put_object(
            Key=f'{date_time.strftime("%m-%d-%y")}/{bucket_name}-{date_time.strftime("%H:%M:%S")}.parquet',
            Body=buffer.getvalue()
        )


def transform_and_save_to_parquet(**kwargs):
    """Function that transform and save json files to parquet format in bucket"""
    exchanger = kwargs["exchanger"]
    s3_connection = get_s3_connection()
    spark = get_spark_session()
    bucket = s3_connection.Bucket(exchanger)
    keys = get_json_file_keys(bucket)
    if keys:
        dataframe: DataFrame = get_dataframe_from_json_files(spark, s3_connection, exchanger, keys)
        dataframe.show()
        dataframe = transform_dataframe(dataframe, exchanger)
        dataframe.show()
        save_dataframe_to_parquet(dataframe, s3_connection, exchanger)
