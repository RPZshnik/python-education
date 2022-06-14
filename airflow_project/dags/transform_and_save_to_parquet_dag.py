"""DAG for transform and save raw data in parquet format"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from spark_jobs.manage_buckets_job import create_bucket, clear_bucket

from spark_jobs.transform_and_save_to_parquet_job import transform_and_save_to_parquet


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    'start_date': datetime(2022, 1, 1, 0, 0),
    'max_active_runs': 1,
    'retry_delay': timedelta(minutes=5),
    "is_paused_upon_creation": False
}

services = ['bitfinex', 'bitmex', 'poloniex']


with DAG("transform_and_save_to_parquet_dag", schedule_interval="0 * * * *",
         default_args=default_args, catchup=False) as dag:
    parquet_operators = []
    bucket_create_operators = []
    bucket_clear_operators = []

    for exchange in services:
        operator = PythonOperator(
            task_id=f'create_{exchange}_parquet_bucket',
            python_callable=create_bucket,
            op_kwargs={'exchanger': exchange + "_parquet"}
        )
        bucket_create_operators.append(operator)

    for exchange in services:
        operator = PythonOperator(
            task_id=f'transform_and_save_{exchange}_to_parquet',
            python_callable=transform_and_save_to_parquet,
            op_kwargs={'exchanger': exchange}
        )
        parquet_operators.append(operator)

    for exchange in services:
        operator = PythonOperator(
            task_id=f'clear_{exchange}_bucket',
            python_callable=clear_bucket,
            op_kwargs={'bucket_name': exchange}
        )
        bucket_clear_operators.append(operator)

    for create, parquet, clear in zip(bucket_create_operators,
                                      parquet_operators,
                                      bucket_clear_operators):
        create >> parquet >> clear
