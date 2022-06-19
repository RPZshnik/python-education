"""DAG that derive imdb data"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from jobs.derive_imdb_data_job import derive_imdb_data

start_datetime = datetime(2022, 6, 11, 11, 30, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("derive_imdb_data_dag", default_args=default_args,
         schedule_interval="0 3 * * *", catchup=False) as dag:

    derive_data = PythonOperator(
        task_id=f'derive_imdb_data',
        python_callable=derive_imdb_data,
    )
