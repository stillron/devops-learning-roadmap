import os
import logging
import sys
import requests
import random
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from events import Event

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Setup Jinja2 Environment
env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    autoescape=select_autoescape()
)

template = env.get_template("impress.j2")

client_id = os.environ['API_CLIENT_ID']
client_secret = os.environ['API_TOKEN']

logger.info("Authenicating with LibCal API")
try:
    r = requests.post('https://leblibrary.libcal.com/1.1/oauth/token',
                    json={"client_id": client_id,
                            "client_secret": client_secret,
                            "grant_type": "client_credentials"})
    r.raise_for_status()
    access_token = r.json().get('access_token')
    if not access_token:
        logger.error("No access token in response")
        sys.exit(1)
    logger.info("Successfully authenticated")
except requests.exceptions.RequestException as e:
    logger.error(f"OAuth failed: {e}")
    sys.exit(1)

events_headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': f"Bearer {access_token}"}

# Fetch events
logger.info("Fetching events from calendars")
kilton_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=15144', headers=events_headers).json()
logger.info(f"Kilton: {len(kilton_events.get('events', []))} events")

leb_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=17790', headers=events_headers).json()
logger.info(f"Lebanon: {len(leb_events.get('events', []))} events")

outreach_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=21747', headers=events_headers).json()
logger.info(f"Outreach: {len(outreach_events.get('events', []))} events")

unsorted_events = kilton_events['events'] + leb_events['events'] + outreach_events['events']
logger.info(f"Total events: {len(unsorted_events)}")

Event.add_events(unsorted_events)
arrangement = Event.arrange()
logger.info(f"Using arrangement: {arrangement}")

#Render
output = template.render({"events": Event.list_events()})
logger.info("Rendered template successfully")

with open('output/index.html', 'w') as writer:
    writer.write(output)
logger.info("Wrote output/index.html")