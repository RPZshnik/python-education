"""DAG to load movies to postgres"""
from datetime import timedelta
from os import environ

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime
from jobs.load_data_to_postgres_job import load_data_to_postgres

from manage.manage_postgres import create_db
from manage.manage_buckets import clear_bucket

start_datetime = datetime(2021, 6, 20, 0, 0, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("load_data_to_postgres_dag", default_args=default_args,
         schedule_interval="0 1 * * *", catchup=False) as dag:

    bucket_name = environ.get("MINIO_RAW_DATA_BUCKET_NAME")
    db_name = environ.get("FILMS_POSTGRES_TABLE_NAME")

    create_db = PythonOperator(
        task_id="create_db",
        python_callable=create_db,
        op_kwargs={"db_name": db_name}
    )

    save = PythonOperator(
        task_id='load_data_to_postgres',
        python_callable=load_data_to_postgres,
    )

    clear = PythonOperator(
        task_id="clear_films_bucket",
        python_callable=clear_bucket,
        op_kwargs={"bucket_name": bucket_name}
    )

    create_db >> save >> clear
