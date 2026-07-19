import pandas as pd
from sqlalchemy import create_engine

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "uber_eats"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def run_query(query):
    """
    Executes a SQL query and returns the result as a Pandas DataFrame.
    """
    return pd.read_sql(query, engine)


def test_connection():
    try:
        with engine.connect():
            return True
    except Exception as e:
        return str(e)