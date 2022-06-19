"""DAG to load movies to postgres"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime
from jobs.load_data_to_postgres_job import load_data_to_postgres

from jobs.manage_buckets import clear_bucket
from jobs.manage_postgres import create_db

start_datetime = datetime(2022, 6, 11, 11, 30, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("load_data_to_postgres_dag", default_args=default_args,
         schedule_interval="0 2 * * *", catchup=False) as dag:

    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")

    create_db = PythonOperator(
        task_id="create_db",
        python_callable=create_db,
        op_kwargs={"db_name": "films"}
    )

    save = PythonOperator(
        task_id='load_data_to_postgres',
        python_callable=load_data_to_postgres,
    )

    # clear_bucket = PythonOperator(
    #     task_id="clear_films_bucket",
    #     python_callable=clear_bucket,
    #     op_kwargs={"bucket_name": bucket_name}
    # )

    create_db >> save
