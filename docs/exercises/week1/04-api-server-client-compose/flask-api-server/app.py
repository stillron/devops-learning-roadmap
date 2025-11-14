from flask import Flask
from flask import request

app = Flask(__name__)

containers = [
    {"name": "nginx-proxy", "image": "nginx:latest", "ports": [80, 443], "status": "running"},
    {"name": "postgres-db", "image": "postgres:15", "ports": [5432], "status": "running"},
    {"name": "redis-cache", "image": "redis:7", "ports": [6379], "status": "stopped"},
    {"name": "app-api", "image": "myapp:v2", "ports": [8000, 8001], "status": "running"}
]

def containers_to_json():
    servers = {"containers":{}, "summary": {"total":0, "running":0, "stopped":0}}

    servers["containers"] = {
    v['name']: {
        "id": i,
        "image": v['image'],
        "port_count": len(v['ports']),
        "ports": ", ".join([str(x) for x in v['ports']]),
        "status": v["status"]
    }
    for i, v in enumerate(containers)
    }

    servers["summary"]["total"] = len(containers)

    for container in containers:
        if container["status"] == "running":
            servers["summary"]["running"] += 1
        else:
            servers["summary"]["stopped"] += 1

    return servers




@app.get("/")
def welcome():
    return "<p>Hello, World!</p>"

@app.get("/containers")
def list_containers():
    return containers_to_json()

@app.get("/container/<name>")
def show_container(name):
        container = [container for container in containers if container['name'] == name]
        if len(container) == 1:
            return container[0]
        else:
            return f"Couldn't find container with name: {name}"

@app.post("/container")
def add_container():
    container_data = request.json
    containers.append(container_data)
    return {"message": f"Added container: {container_data['name']}"}, 201

@app.put("/container")
def update_container():
    container_data = request.json
    con_list = [container for container in containers if container['name'] == container_data['name']]
    if len(con_list) == 1:
        container = con_list[0]
        container['name'] = container_data['name']
        container['image'] = container_data['image']
        container['ports'] = container_data['ports']
        container['status'] = container_data['status']
        return {"message":f"Updated container: {container['name']}"}, 200
    else:
        return {f"Container {container_data['name']} does not exist"}, 404

@app.delete("/container")
def delete_container():
    container_data = request.json
    con_list = [i for i,x in enumerate(containers) if x['name'] == container_data['name']]
    if len(con_list) == 1:
        index = con_list[0]
        del containers[index]
        return {"message": f"Deleted container with name: {container_data['name']}"}, 200
    else:
        return {"message": f"No container with name: {container_data['name']}"},404
        