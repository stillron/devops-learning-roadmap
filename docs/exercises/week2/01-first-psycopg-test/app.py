from flask import Flask
from flask import request
import psycopg
from psycopg.rows import dict_row

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello World!"

@app.get("/message")
def show_messages():
    with psycopg.connect("dbname=test_db user=ron.houk", row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            records =  cur.execute("SELECT * from test_messages").fetchall()

    return records

@app.post("/message")
def add_message():
    message = request.json['message']

    with psycopg.connect("dbname=test_db user=ron.houk", row_factory=dict_row) as conn:
        with conn.cursor() as cur:

            cur.execute("""
            INSERT INTO test_messages (message)
            VALUES (%s)
            RETURNING id, message;
            """,
            (message,))

            inserted = cur.fetchone()
    return {"message": "Success!", "inserted": inserted}