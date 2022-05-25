from botocore.config import Config
from sqlalchemy import create_engine
from io import StringIO
from os import environ
import pandas
import boto3


def get_s3_connection():
    user = environ.get('MINIO_ROOT_USER')
    password = environ.get('MINIO_ROOT_PASSWORD')
    session = boto3.session.Session()
    s3_connection = session.resource(
        's3',
        endpoint_url='http://s3:9000',
        aws_access_key_id=user,
        aws_secret_access_key=password,
        config=Config(signature_version='s3v4'),
        region_name='us-west-1'
    )
    return s3_connection


def get_db_connection():
    db_password = environ.get('POSTGRES_PASSWORD')
    db_connection = create_engine(f'postgresql+psycopg2://postgres:{db_password}@database:5432/postgres')
    return db_connection


def get_csv_files(bucket):
    for obj in bucket.objects.all():
        csv_file = obj.get()['Body'].read()
        decoded_csv_file = StringIO(csv_file.decode('utf-8'))
        yield decoded_csv_file


def translate_df_columns(dataframe):
    """Function rename (translate) dataframe's columns"""
    columns = {
        'data': 'date',
        'stato': 'country',
        'codice_regione': 'region_code',
        'denominazione_regione': 'region_name',
        'codice_provincia': 'province_code',
        'denominazione_provincia': 'province_name',
        'sigla_provincia': 'province_abbreviation',
        'lat': 'latitude',
        'long': 'longitude',
        'totale_casi': 'cases_amount',
        'note': 'note',
               }
    dataframe.rename(columns=columns, inplace=True)


def change_type(data_frame):
    """Function change type of date column"""
    data_frame['date'] = pandas.to_datetime(data_frame['date'],
                                            format='%Y-%m-%d %H:%M:%S')


def import_df_to_db(db_connection, data_frame):
    """Function import data frame to database"""
    data_frame.to_sql('postgres', db_connection,
                      index=False, if_exists='append')


def main():
    """Main function"""
    s3_connection = get_s3_connection()
    db_connection = get_db_connection()
    bucket_name = environ.get('BUCKET_NAME')
    bucket = s3_connection.Bucket(bucket_name)
    csv_files = get_csv_files(bucket)
    dataframe = pandas.concat(map(pandas.read_csv, csv_files))
    translate_df_columns(dataframe)
    change_type(dataframe)
    import_df_to_db(db_connection, dataframe)


if __name__ == '__main__':
    main()
