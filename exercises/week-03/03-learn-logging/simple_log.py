import logging
from pythonjsonlogger.json import JsonFormatter

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler (this is the "where does it go?" part)
shandler = logging.StreamHandler()
fhandler = logging.FileHandler('app.log')

# Create a formatter (this is the "what does it look like?" part)
sformatter = logging.Formatter(' %(asctime)s - %(levelname)s - %(message)s')
fformatter = JsonFormatter('%(created)s %(levelname)s %(name)s %(pathname)s %(funcName)s %(lineno)d %(message)s')

# Attach formatter to handler
shandler.setFormatter(sformatter)
fhandler.setFormatter(fformatter)


# Attach the handler to the logger
logger.addHandler(shandler)
logger.addHandler(fhandler)

logger.info("This is a test message")
logger.info("First message")
logger.warning("Second message")
logger.error("Third message")