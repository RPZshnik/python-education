
# DE_FINAL_PROJECT


Data pipeline with a Metabase dashboard with Airflow orchestration and Spark jobs.

### Main components
##### Airflow  - orchestrates data pipeline
##### Pyspark - used for transform the data
##### PostgreSQL - used for storing transformed data
##### S3(minio) - AWS cloud storage used as a storage for raw data
##### Metabase - is an open source business intelligence tool. It lets you ask questions about your data, and displays answers in formats that make sense, whether that's a bar chart or a detailed table.

Getting Started
---------------

Set up credentials (in e.g. ~/.env/):

.. code-block:: ini

    MINIO_ROOT_USER=YOUR_MINIO_ACCESS_KEY
    MINIO_ROOT_PASSWORD=YOUR_MINIO_SECRET_KEY
    MINIO_RAW_DATA_BUCKET_NAME=YOUR_MINIO_RAW_DATA_BUCKET_NAME
    MINIO_IMDB_DATA_BUCKET_NAME=YOUR_MINIO_IMDB_DATA_BUCKET_NAME
    
    AIRFLOW_USERNAME=YOUR_AIRFLOW_USERNAME
    AIRFLOW_FIRSTNAME=YOUR_AIRFLOW_FIRSTNAME
    AIRFLOW_LASTNAME=YOUR_AIRFLOW_LASTNAME
    AIRFLOW_EMAIL=YOUR_AIRFLOW_EMAIL
    AIRFLOW_PASSWORD=YOUR_AIRFLOW_PASSWORD
    
    POSTGRES_USER=YOUR_POSTGRES_USER
    POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD
    POSTGRES_DB=YOUR_POSTGRES_DB
    POSTGRES_PORT=5432
    
    TMDB_API_KEY=YOUR_TMDB_API_KEY
    
    FILMS_POSTGRES_TABLE_NAME=YOUR_FILMS_POSTGRES_TABLE_NAME
    
    MB_DB_TYPE=postgres
    MB_DB_PORT=5432
    MB_DB_USER=YOUR_POSTGRES_USER
    MB_DB_PASS=YOUR_POSTGRES_PASSWORD
    MB_DB_HOST=YOUR_MB_DB_HOST

Then, assuming that you have a supported version of docker-compose installed, you can start the project with:

.. code-block:: sh

    $ sudo docker-compose up


Using:
---------------
After starting the project, you can open Airflow UI with: http://localhost:8000


![](https://i.ibb.co/Pz7yhRC/image.png)


After entering the credentials, you will be able to see Airflow UI and start the dags


![](https://i.ibb.co/5FTrCTH/image.png)



After working out the pipeline, you can open metabase UI with for working with dashboards: http://localhost:3001


Examples:
---------------



### Metabase

![](https://i.ibb.co/6tx3bsP/image.png)


![](https://i.ibb.co/zZnqNp8/image.png)

