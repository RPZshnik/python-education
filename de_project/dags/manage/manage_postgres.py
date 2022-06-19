"""Module that implement manage of postgres db"""
import logging
from os import environ
import pandas as pd
from sqlalchemy import create_engine


def get_db_connection(db_name=None):
    """Function create and return db connection"""
    db_user = environ.get("POSTGRES_USER")
    db_port = environ.get("POSTGRES_PORT")
    db_password = environ.get('POSTGRES_PASSWORD')
    if db_name is None:
        db_connection = create_engine(f'postgresql+psycopg2://{db_user}:'
                                      f'{db_password}@database:{db_port}')
    else:
        db_connection = create_engine(f'postgresql+psycopg2://{db_user}:'
                                      f'{db_password}@database:{db_port}/{db_name}')
    return db_connection


def create_db(db_name: str):
    """Function that create database"""
    db_connection = get_db_connection().connect().execution_options(isolation_level="AUTOCOMMIT")
    try:
        db_connection.execute(f"CREATE DATABASE {db_name};")
    except Exception as error:
        logging.warning(error)
    finally:
        db_connection.close()


def load_table_from_postgres(table_name: str, db_name=None):
    """Function load db table and return dataframe"""
    db_connection = get_db_connection(db_name).connect()
    dataframe = pd.read_sql(f"SELECT * FROM \"{table_name}\"", db_connection)
    db_connection.close()
    return dataframe
