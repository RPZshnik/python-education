"""Job codes for update movies DAG"""
import concurrent.futures
import time
from os import environ
from datetime import datetime, timedelta
import json
import boto3
import requests
from botocore.config import Config
from requests.exceptions import RequestException


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


def __get_api_link(start_parse_date: datetime, end_parse_date: datetime):
    """Function that build api_link and return it"""
    api_key = environ.get('TMDB_API_KEY')
    api_link = (f"https://api.themoviedb.org/3/discover/movie?"
                f"api_key={api_key}&"
                f"sort_by=primary_release_date.desc&"
                f"primary_release_date.lte={end_parse_date.strftime('%Y-%m-%d')}&"
                f"primary_release_date.gte={start_parse_date.strftime('%Y-%m-%d')}&"
                f"page=%s")
    return api_link


def __get_amount_of_pages(api_link):
    """Function that return amount of film's pages"""
    response = requests.get(api_link).json()
    amount_of_pages = response["total_pages"]
    return amount_of_pages


def __get_id_of_movies_per_day(date: datetime):
    """Function that parse and return movies' id by date"""
    api_link = __get_api_link(date, date)
    amount_of_pages = __get_amount_of_pages(api_link)
    movies_id = []
    session = requests.session()
    for page in range(1, amount_of_pages + 1):
        response = session.get(api_link % page)
        if response.status_code == 200:
            movies_id.extend([movie["id"] for movie in response.json()["results"]])
        else:
            raise RequestException("Invalid url")
    return movies_id


def __get_data_per_day(date: datetime):
    """Function that parse and return films data by date"""
    api_key = environ.get('TMDB_API_KEY')
    link = "https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    session = requests.session()
    api_links = [link.format(movie_id=movie_id, api_key=api_key)
                 for movie_id in __get_id_of_movies_per_day(date)]

    def load_url(url):
        response = session.get(url)
        return response.json()

    def get_results(future_to_url):
        for future in concurrent.futures.as_completed(future_to_url):
            if future.result()["imdb_id"] is None:
                continue
            yield future.result()
            time.sleep(0.005)

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        day_data = get_results((executor.submit(load_url, url) for url in api_links))
        data_bytes_format = bytes(json.dumps(list(day_data), indent=2),
                                  encoding="utf-8")
    return data_bytes_format


def __save_to_minio(connection, bucket_name, data, movies_date):
    """Function that implement data to minio"""
    movies_date = movies_date.strftime('%Y-%m-%d')
    connection.Bucket(bucket_name).put_object(Body=data,
                                              Key=f'{movies_date}/tmdb_data.json')


def update_movies():
    """Function that implement parse and save data to minio"""
    s3_connection = __get_s3_connection()
    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    today_date = datetime.now() - timedelta(days=1)
    data = __get_data_per_day(today_date)
    __save_to_minio(s3_connection, bucket_name, data, today_date)
