"""Job codes for save movies range DAG"""
import concurrent.futures
import logging
import time
from os import environ
from datetime import datetime, timedelta
import json
import requests
from requests.exceptions import RequestException

from manage_buckets import get_s3_connection

DEFAULT_START_DATE = "2020-01-01"


def __get_start_parse_date(**context) -> datetime:
    try:
        start_parse_date = context['dag_run'].conf['start_parse_date']
        start_parse_date = datetime.strptime(start_parse_date, "%Y-%m-%d")
    except KeyError:
        start_parse_date = datetime.strptime(DEFAULT_START_DATE, "%Y-%m-%d")
    return start_parse_date


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
        response = session.get(url, headers={'Accept-Encoding': 'identity'})
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


def __get_data(start_parse_date: datetime):
    """Function get and return data by api link in byte format"""
    end_parse_date = datetime.now() - timedelta(days=1)
    time_delta = (end_parse_date - start_parse_date).days
    for days_delta in range(time_delta):
        current_date = end_parse_date - timedelta(days=days_delta)
        try:
            data_per_day = __get_data_per_day(current_date)
            yield data_per_day, current_date
        except Exception as error:
            logging.error(error)


def __save_to_minio(connection, bucket_name, data):
    """Function that implement data to minio"""
    for json_data, movies_date in data:
        movies_date = movies_date.strftime('%Y-%m-%d')
        connection.Bucket(bucket_name).put_object(Body=json_data,
                                                  Key=f'{movies_date}/tmdb_data.json')


def save_movies_range(**context):
    """Function that implement parse and save data to minio"""
    s3_connection = get_s3_connection()
    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    start_parse_date = __get_start_parse_date(**context)
    json_data_with_date = __get_data(start_parse_date)
    __save_to_minio(s3_connection, bucket_name, json_data_with_date)
