from dotenv import load_dotenv
import os
from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row
import atexit

load_dotenv()

db_name = os.getenv('POSTGRES_DB')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_DBHOST')
db_user = os.getenv('POSTGRES_USER')
conn_string = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

try:
    pool = ConnectionPool(conninfo=conn_string, open=True, timeout=2, kwargs={"row_factory": dict_row})

except Exception as error:
    print("Error while connecting to PostgreSQL", error)
    pool = None
finally:
    if pool:
        atexit.register(pool.close)