from flask import Flask
import psycopg
from psycopg.rows import dict_row

app = Flask(__name__)

@app.get("/")
def hello_world():
    with psycopg.connect("dbname=test_db user=ron.houk", row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            records =  cur.execute("SELECT * from test_messages").fetchall()

    return records