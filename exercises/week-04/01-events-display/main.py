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

r = requests.post('https://leblibrary.libcal.com/1.1/oauth/token',
                  json={"client_id": client_id,
                        "client_secret": client_secret,
                        "grant_type": "client_credentials"})


access_token = r.json().get('access_token')

events_headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': f"Bearer {access_token}"}

kilton_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=15144', headers=events_headers).json()
leb_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=17790', headers=events_headers).json()
outreach_events = requests.get('https://leblibrary.libcal.com/1.1/events?cal_id=21747', headers=events_headers).json()

unsorted_events = kilton_events['events'] + leb_events['events'] + outreach_events['events']

Event.add_events(unsorted_events)
Event.arrange()
arrangement = Event.arrangement
logger.info(f"Using arrangement: {arrangement}")
output = template.render({"events": Event.list_events()})

with open('output/index.html', 'w') as writer:
    writer.write(output)