"""Module for manage buckets (create, clear, etc.)"""
import logging
from os import environ
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError


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


def create_bucket(**kwargs):
    """Function for create the bucket by name"""
    exchanger = kwargs['exchanger']
    s3_connection = get_s3_connection()
    try:
        s3_connection.create_bucket(Bucket=exchanger)
    except ClientError as error:
        logging.error(error)


def clear_bucket(**kwargs):
    """Function that delete all objects from bucket"""
    bucket_name = kwargs["bucket_name"]
    s3_connection = get_s3_connection()
    s3_connection.Bucket(bucket_name).objects.all().delete()
