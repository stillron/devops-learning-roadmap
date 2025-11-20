from flask import Flask, request
from db import pool

app = Flask(__name__)

@app.get("/containers")
def get_all_containers():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            containers = cur.execute("SELECT * from containers").fetchall()

    return containers, 200