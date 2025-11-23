from flask import Flask, request
from psycopg import sql
from db import pool

app = Flask(__name__)

def build_container(r):
    container = {}
    container['name'] = r.json.get('name')
    container['image'] = r.json.get('image')
    container['ports'] = r.json.get('ports')
    container['status'] = r.json.get('status')
    if not container['name'] or not container['image'] or not container['ports'] or not container['status']:
        return None
    else:
        return container

@app.get("/containers")
def get_all_containers():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            containers = cur.execute("SELECT * from containers").fetchall()

    return containers, 200

@app.get("/container/<int:id>")
def get_container(id):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            container = cur.execute("SELECT * FROM containers WHERE id = %s", (id,)).fetchone()
    if container:
        return {"message": "Success", "container": container}, 200
    else:
        return {"message": "Failed", "err": f"Container id {id} not found."}, 404

@app.post("/container")
def insert_container():
    container = build_container(request)
    if not container:
        return {"message": "Failed", "err": "Container data must include name, image, ports, and status"}, 400
    

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO containers (name, image, ports, status) 
            VALUES (%s, %s, %s, %s)
            RETURNING id, name, image, ports, status;
            """,
            (container['name'], container['image'], container['ports'], container['status']))

            result = cur.fetchone()
    
    if result:
        return {"message": "Container created", "container": result}, 201
    else:
        return {"message": "Failed", "err": f"Failed to insert container data {container}"}, 500

@app.put("/container/<int:id>")
def update_container(id):
    container = build_container(request)
    if not container:
        return {"message": "Failed", "err": "Container data must include name, image, ports, and status"}, 400

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE containers
            SET name = %s,
                image = %s,
                ports = %s,
                status = %s
            WHERE id = %s
            RETURNING id, name, image, ports, status;
            """,
            (container['name'], container['image'], container['ports'], container['status'], id))

            result = cur.fetchone()
    if result:
        return {"message": "Container updated", "container": result}, 200
    else:
        return {"message": "Failed", "err": f"Container id {id} not found"}, 404

@app.patch("/container/<int:id>")
def patch_container(id):
    update_data = request.json

    if not update_data:
        return {"message": "Failed", "err": "No fields provided to update"}, 400

    allowed_keys = True

    for k in update_data.keys():
        if k not in ('name', 'image', 'ports', 'status'):
            allowed_keys = False

    if not allowed_keys:
        return {"message": "Failed", "err": "Keys can only be 'name', 'image', 'ports', or 'status'"}

    set_clauses = []
    values = []

    for key, value in update_data.items():
        set_clauses.append(sql.SQL("{} = %s").format(sql.Identifier(key)))
        values.append(value)

    fields = sql.SQL(', ').join(set_clauses)
    query = sql.SQL("UPDATE containers SET {} WHERE id = %s RETURNING id, name, image, ports, status;").format(fields)

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (*values, id))

            result = cur.fetchone()
        
        if result:
            return{"message": "Container patched", "container": result}, 200
        else:
            return{"message": "Failed", "err": f"Container id {id} not found"}, 404


@app.delete("/container/<int:id>")
def delete_container(id):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM containers
            WHERE id = %s
            RETURNING id, name, image, ports, status;
            """,
            (id,))
    
            result = cur.fetchone()
    if result:
        return {"message": "Container deleted", "container": result}, 200
    else:
        return {"message": "Failed", "err": f"Container id {id} not found"}, 404