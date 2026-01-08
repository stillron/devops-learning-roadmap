import os
import sys
import logging
from dotenv import load_dotenv
import requests
import json
from datetime import datetime as dt
from bookings import Booking

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

API_CLIENT_ID = os.environ["API_CLIENT_ID"]
API_TOKEN = os.environ["API_TOKEN"]


def fetch_and_save_bookings():
    os.makedirs('data', exist_ok=True)
    logger.info("Authenticating with LibCal API")
    
    try:
        r = requests.post(
            "https://leblibrary.libcal.com/1.1/oauth/token",
            json={
                "client_id": API_CLIENT_ID,
                "client_secret": API_TOKEN,
                "grant_type": "client_credentials",
            },
        )
        r.raise_for_status()
        access_token = r.json().get("access_token")
        if not access_token:
            logger.error("No access token in response")
            return False
        logger.info("Successfully authenticated")
    except requests.exceptions.RequestException as e:
        logger.error(f"Oauth failed: {e}")
        return False

    bookings_headers = {
        "Content-type": "application/json",
        "Accept": "text/plain",
        "Authorization": f"Bearer {access_token}",
    }

    logger.info("Fetching bookings from calendars")
    try:
        # days query parameter defaults to 0 so 6 is actually 7 days
        bookings = requests.get(
            "https://leblibrary.libcal.com/1.1/space/bookings?days=6&include_cancel=0&limit=500&internal_notes=true",
            headers=bookings_headers,
        ).json()
        logger.debug(bookings)
    except Exception as e:
        logger.error(f"API fetch failed: {e}")
        return False

    logger.info(f"Retrieved {len(bookings)} bookings")

    all_bookings = [Booking(booking) for booking in bookings]

    bookings_data = [booking.to_dict() for booking in all_bookings]

    timestamp = dt.now().isoformat()

    bookings_with_info = {
        "last_updated": timestamp,
        "bookings": bookings_data
    }

    try:
        with open('data/bookings.json', 'w') as f:
            json.dump(bookings_with_info, f, indent=2)
        logger.info("Wrote bookings to 'data/bookings.json'")
        return True
    except Exception as e:
        logger.error(f"Error writing bookings to file: {e}")
        return False

if __name__ == "__main__":
    fetch_and_save_bookings()