import logging
from os import environ

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists


def get_db_connection():
    db_user = environ.get("POSTGRES_USER")
    db_port = environ.get("POSTGRES_PORT")
    db_password = environ.get('POSTGRES_PASSWORD')
    db_connection = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@database:{db_port}')
    return db_connection


def create_db(db_name: str):
    db_connection = get_db_connection().connect().execution_options(isolation_level="AUTOCOMMIT")
    try:
        db_connection.execute(f"CREATE DATABASE {db_name};")
    except Exception as error:
        logging.warning(error)
    finally:
        db_connection.close()
