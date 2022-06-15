"""DAG for save raw data in json format"""
from datetime import timedelta
from airflow import DAG
from airflow.models.dag import get_last_dagrun
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import datetime
from airflow.utils.session import provide_session

from spark_jobs.manage_buckets_job import create_bucket
from spark_jobs.temporary_storage_job import save_json_to_minio

start_datetime = datetime(2022, 6, 11, 11, 30, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': datetime(2021, 8, 29, 16, 00),
    'retry_delay': timedelta(minutes=5),
    "is_paused_upon_creation": False
}

services = {
    'bitfinex': {'link': 'https://api.bitfinex.com/v1/trades/btcusd?start={}&end={}', 'end_start_format': '%s'},
    'bitmex': {'link':
                   'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&startTime={}&endTime={}',
               'end_start_format': '%Y-%m-%d%%20%H%%3A%M'},
    'poloniex': {'link':
                     'https://poloniex.com/public?command=returnTradeHistory&currencyPair=USDT_BTC&start={}&end={}',
                 'end_start_format': '%s'}
}


@provide_session
def _get_execution_date_of_dag(query, session=None, **kwargs):
    dag_last_run = get_last_dagrun(
        'transform_and_save_to_parquet_dag', session)
    return dag_last_run.execution_date


with DAG("temporary_storage_dag", default_args=default_args,
         schedule_interval="*/1 * * * *", catchup=False) as dag:
    external_sensor_operators = []
    json_operators = []
    bucket_operators = []
    for exchange in services:
        sensor = ExternalTaskSensor(
            task_id=f'external_sensor_{exchange}',
            external_dag_id='transform_and_save_to_parquet_dag',
            poke_interval=5,
            execution_date_fn=_get_execution_date_of_dag
        )
        external_sensor_operators.append(sensor)

    for exchange in services:
        operator = PythonOperator(
            task_id=f'create_{exchange}_bucket',
            python_callable=create_bucket,
            op_kwargs={'exchanger': exchange}
        )
        bucket_operators.append(operator)

    for exchange, info in services.items():
        operator = PythonOperator(
            task_id=f'save_{exchange}_json_to_minio',
            python_callable=save_json_to_minio,
            op_kwargs={'exchanger': exchange, 'link': info['link'], 'end_start_format': info['end_start_format']}
        )
        json_operators.append(operator)

    for bucket, json, sensor in zip(bucket_operators,
                                    json_operators,
                                    external_sensor_operators):
        sensor >> bucket >> json
