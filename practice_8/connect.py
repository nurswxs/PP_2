import psycopg2
from config import load_config

def connect():
    config = load_config()

    try:
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL")
        return conn
    except Exception as error:
        print(error)
        return None
