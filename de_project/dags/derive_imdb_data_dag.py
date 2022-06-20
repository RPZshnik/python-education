"""DAG that derive imdb data"""
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import datetime

from jobs.derive_imdb_data_job import derive_imdb_data

start_datetime = datetime(2021, 6, 20, 0, 0, 0, 0)

default_args = {
    "owner": "airflow",
    'max_active_runs': 1,
    "depends_on_past": False,
    'start_date': start_datetime,
    'retry_delay': timedelta(minutes=5)
}


with DAG("derive_imdb_data_dag", default_args=default_args,
         schedule_interval="0 1 * * *", catchup=False) as dag:

    ext_sensor = ExternalTaskSensor(
        task_id='check_load_to_db',
        external_dag_id='load_data_to_postgres_dag',
    )

    derive_data = PythonOperator(
        task_id='derive_imdb_data',
        python_callable=derive_imdb_data,
    )

    ext_sensor >> derive_data
