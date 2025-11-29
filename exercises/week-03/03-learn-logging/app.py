import logging
from flask import Flask
from pythonjsonlogger import jsonlogger

# Create a JSON formatter
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(pathname)s %(funcName)s %(lineno)d %(message)s')
logHandler.setFormatter(formatter)

# Setup the logger
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.get("/")
def hello():
    logger.info("Hello endpoint was called", extra={"endpoint": "/", "method": "GET"})
    return {"msg": "Hello World!"}, 200