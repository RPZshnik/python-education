"""DAG for update movies"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from jobs.update_movies_job import update_movies


start_datetime = datetime(2022, 6, 11, 11, 30, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("update_movies_dag", default_args=default_args,
         schedule_interval="35 1 * * *", catchup=False) as dag:

    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")

    save_operator = PythonOperator(
        task_id='update_movies',
        python_callable=update_movies,
        provide_context=True
    )
