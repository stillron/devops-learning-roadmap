from flask import Flask, request, render_template

# from flask_cors import CORS
import logging
import json
from datetime import datetime as dt
from datetime import datetime, date, timedelta
from fetcher import fetch_and_save_bookings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# CORS(app)

# ============================================================================
# Constants
# ============================================================================
CUTOFF_HOURS = {
    0: 18,  # Monday
    1: 18,  # Tuesday
    2: 18,  # Wednesday
    3: 18,  # Thursday
    4: 17,  # Friday
    5: 17,  # Saturday
    6: 0,  # Sunday
}

SPACES = {
    106060: "Community Room",
    106062: "Conference Room",
    118237: "Tutorial Room",
    120550: "Damren Room",
    120553: "Rotary Room",
    124474: "The Arcade",
}

# ============================================================================
# Helper Functions
# ============================================================================

def check_after_hours(end_time_iso_string: str) -> bool:
    end_dt = dt.fromisoformat(end_time_iso_string)
    end_day_of_week = end_dt.weekday()
    end_hour = end_dt.hour
    end_minute = end_dt.minute
    end_dt_cutoff_hour = CUTOFF_HOURS[end_day_of_week]

    if end_hour > end_dt_cutoff_hour or (
        end_hour == end_dt_cutoff_hour and end_minute > 0
    ):
        return True
    else:
        return False

def get_space_id_from_request() -> int :
    """Get and validate space_id from request args, defaulting to Community Room (106060)"""
    try:
        space_id = int(request.args.get("id", 106060))
    except ValueError as e:
        logger.info(f"Invalid query parameter: {e}")
        space_id = 106060
    return space_id

def get_booking_data() -> dict:
    """Load bookings from JSON file. Raises exception if file can't be read."""

    with open("data/bookings.json", "r") as f:
        return json.load(f)


def group_bookings_by_day(booking_info: dict, space_id: int) -> list:
    """Group bookings into days with labels"""

    days_list = []
    all_bookings = booking_info["bookings"]
    filtered_bookings = [
        booking for booking in all_bookings if booking.get("space_id") == space_id
    ]

    today = date.today()
    tomorrow = today + timedelta(days=1)

    days = [today, tomorrow]
    logger.info(f"Grouping {len(filtered_bookings)} bookings for space {space_id}")

    for i in range(2, 7):
        days.append(today + timedelta(days=i))

    for day in days:
        if day == today:
            days_list.append({"day": "Today", "date": day, "bookings": []})
        elif day == tomorrow:
            days_list.append({"day": "Tomorrow", "date": day, "bookings": []})
        else:
            days_list.append(
                {"day": f"{day.strftime("%A")}", "date": day, "bookings": []}
            )

    for day in days_list:
        for booking in filtered_bookings:
            booking_date = datetime.fromisoformat(booking["start"]).date()
            if day["date"] == booking_date:
                booking["after_hours"] = check_after_hours(booking["end"])
                day["bookings"].append(booking)
                logger.debug(f"Appending {booking.get('id')}")
        day["bookings"].sort(key=lambda booking: booking["start"])
        logger.debug(f"{len(day['bookings'])} bookings for {day['day']}")
    return days_list


# ============================================================================
# Template Functions
# ============================================================================

@app.template_filter("format_timestamp")
def format_timestamp(iso_string):
    formatted_string = dt.fromisoformat(iso_string).strftime(
        "%a, %b. %d %Y at %-I:%M%p"
    )
    return formatted_string


@app.template_filter("format_time")
def format_time(iso_string):
    formatted_time = dt.fromisoformat(iso_string).strftime("%-I:%M%p")
    return formatted_time


@app.template_filter("format_shortdt")
def format_shortdt(iso_string):
    formatted_shortdt = dt.fromisoformat(iso_string).strftime("%x %-I:%M%p")
    return formatted_shortdt

# ============================================================================
# Route Functions
# ============================================================================

@app.get("/")
def bookings():
    space_id = get_space_id_from_request()

    space = {"space_id": space_id, "space_name": SPACES.get(space_id)}

    logger.info(f"Requested space_id is: {space_id}")
    try:
        data = get_booking_data()
        logger.info("Successfully retrieved booking data")
    except Exception as e:
        logger.error(f"Error retrieving bookings from file: {e}")
        return render_template("error.html")

    timestamp = data["last_updated"]
    booking_days = group_bookings_by_day(data, space_id)
    logger.debug(f"Bookings for space_id: {space_id} are: {booking_days}")
    return render_template(
        "bookings.html", timestamp=timestamp, bookings=booking_days, space=space
    )

@app.post("/fetch")
def fetch_bookings():
    """Automated data fetch - called by systemd timer"""
    if fetch_and_save_bookings():
        return {"status": "success"}, 200
    else:
        return {"status": "error"}, 500

@app.post("/refresh")
def refresh():
    """User-initiated refresh - returns HTML for current room"""
    if fetch_and_save_bookings():
        return bookings()
    else:
        return render_template("error.html")