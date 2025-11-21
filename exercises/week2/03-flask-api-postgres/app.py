from flask import Flask, request
from db import pool

app = Flask(__name__)

@app.get("/containers")
def get_all_containers():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            containers = cur.execute("SELECT * from containers").fetchall()

    return containers, 200

@app.post("/container")
def insert_container():
    container = {}
    container['name'] = request.json.get('name')
    container['image'] = request.json.get('image')
    container['ports'] = request.json.get('ports')
    container['status'] = request.json.get('status')
    if not container['name'] or not container['image'] or not container['ports'] or not container['status']:
        return {"message": "Failed", "err": "Container data must include name, image, ports, and status"}, 400
    

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO containers (name, image, ports, status) 
            VALUES (%s, %s, %s, %s)
            RETURNING name, image, ports, status;
            """,
            (container['name'], container['image'], container['ports'], container['status']))

            result = cur.fetchone()
    
    if result:
        return {"message": "Container created", "container": result}, 201
    else:
        return {"message": "Failed", "err": f"Failed to insert container data {container}"}, 500