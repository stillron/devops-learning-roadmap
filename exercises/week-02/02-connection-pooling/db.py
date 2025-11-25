from psycopg_pool import ConnectionPool 
from psycopg.rows import dict_row
import atexit


try:
    print("Hello from db.py")
    pool = ConnectionPool(conninfo="dbname=test_db user=ron.houk", open=True, kwargs={"row_factory": dict_row})
    
except Exception as error:
    print("Error while connecting to PostgreSQL", error)
    pool = None
finally:
    if pool:
        atexit.register(pool.close)

