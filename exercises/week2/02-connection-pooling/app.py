from flask import Flask
from flask import request
from db import pool

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello World!"

@app.get("/message")
def show_messages():
    with pool.connection() as conn:
        with conn.cursor() as cur:

            records =  cur.execute("SELECT * from test_messages").fetchall()

    return records

@app.post("/message")
def add_message():
    message = request.json['message']

    with pool.connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
            INSERT INTO test_messages (message)
            VALUES (%s)
            RETURNING id, message;
            """,
            (message,))

            inserted = cur.fetchone()
    if inserted:
        return {"message": "Success!", "inserted": inserted}, 201
    else:
        return {"message": "Failed", "err": f"Failed to insert message {message}"}, 500

@app.delete("/message/<int:id>")
def remove_message(id):
    with pool.connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
            DELETE FROM test_messages WHERE id = %s
            RETURNING *""",
            (id,));

            deleted = cur.fetchone()
    if deleted:
        return {"message": "Success!", "deleted": deleted}, 200
    else:
        return {"message": "Failed", "err": f"id {id} doesn't exist"}, 404

@app.put("/message/<int:id>")
def update_message(id):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            message = request.json["message"]

            cur.execute("""
            UPDATE test_messages
            SET message = %s
            WHERE id = %s
            RETURNING id, message""",
            (message, id));

            updated = cur.fetchone()
    if updated:
        return {"message": "Success!", "updated": updated}, 200
    else:
        return {"message": "Failed", "err": f"id {id} doesn't exist"}, 404