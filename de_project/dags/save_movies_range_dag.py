"""DAG for save raw data in json format"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

from jobs.save_movies_range_job import save_movies_range
from jobs.manage_buckets import create_bucket


start_datetime = datetime(2022, 6, 11, 11, 30, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': datetime(2021, 8, 29, 16, 00),
    'retry_delay': timedelta(minutes=5),
    "is_paused_upon_creation": False
}


with DAG("save_movies_dag", default_args=default_args,
         schedule_interval="@once", catchup=False) as dag:

    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    bucket_create_operator = PythonOperator(
        task_id=f'create_range_bucket',
        python_callable=create_bucket,
        op_kwargs={'bucket_name': bucket_name}
    )

    save_operator = PythonOperator(
        task_id=f'save_movies_range_to_minio',
        python_callable=save_movies_range,
        provide_context=True
    )
    bucket_create_operator >> save_operator
