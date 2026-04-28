import psycopg2              # library for working with PostgreSQL
from config import DB_CONFIG # dictionary with connection parameters from config.py

def get_connection():
    # the function returns a connection to the database
    return psycopg2.connect(**DB_CONFIG)

if __name__ == "__main__":
    conn = get_connection()           # connecting to the database
    print("Соединение установлено!")  # we display the message
    conn.close()                      # closing the connection