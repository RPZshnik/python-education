"""Job code for temporary storage DAG"""
import time
from os import environ
from datetime import datetime
import json
import boto3
import requests
from botocore.config import Config


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


def get_exchanger_data(api_link: str):
    """Function get json file by api link in byte format"""
    response = requests.get(api_link)
    if response.status_code == 200:
        return bytes(json.dumps(response.json(),
                                indent=2), encoding="utf-8")
    return None


def save_json_to_minio(**kwargs):
    """Function for save json files from services to minio"""
    s3_connection = get_s3_connection()

    exchanger = kwargs['exchanger']
    api_link = kwargs['link']
    end_start_format = kwargs['end_start_format']

    timestamp = (time.time() // 60 * 60)
    date_time_start = datetime.utcfromtimestamp(timestamp - 60).strftime(end_start_format)
    date_time_end = datetime.utcfromtimestamp(timestamp).strftime(end_start_format)
    api_link = api_link.format(date_time_start, date_time_end)
    json_data = get_exchanger_data(api_link)
    if json_data is None:
        pass
    s3_connection.Bucket(exchanger).put_object(Body=json_data,
                                               Key=f'{exchanger}-{datetime.now()}.json')
