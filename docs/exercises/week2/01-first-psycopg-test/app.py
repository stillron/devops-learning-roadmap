from flask import Flask
import psycopg

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello world!"