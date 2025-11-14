import requests

r = requests.get('http://localhost:5000/containers')
print(r.json())


payload = {"name": "test-container", "image": "ubuntu:22.04", "ports": [9000], "status": "running"}
r = requests.post('http://localhost:5000/container', json=payload)
print(r.json())

payload =  {"name": "test-container", "image": "ubuntu:22.04", "ports": [9000], "status": "running"}
r = requests.put('http://localhost:5000/container', json=payload)
print(r.json())

payload = {"name": "test-container"}
r = requests.delete('http://localhost:5000/container', json=payload)
print(r.status_code)
print(r.text)

r = requests.get('http://localhost:5000/containers')
print(r.json())

