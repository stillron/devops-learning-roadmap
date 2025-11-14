import requests

r = requests.get('http://flask-api-server:5000/containers')
print(r.json())


payload = {"name": "test-container", "image": "ubuntu:22.04", "ports": [9000], "status": "running"}
r = requests.post('http://flask-api-server:5000/container', json=payload)
print(r.json())

payload =  {"name": "test-container", "image": "ubuntu:22.04", "ports": [9000], "status": "running"}
r = requests.put('http://flask-api-server:5000/container', json=payload)
print(r.json())

payload = {"name": "test-container"}
r = requests.delete('http://flask-api-server:5000/container', json=payload)
print(r.status_code)
print(r.text)

r = requests.get('http://flask-api-server:5000/containers')
print(r.json())

