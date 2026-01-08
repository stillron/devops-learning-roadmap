import datetime as dt


class Booking:
    MINUTES_HOURS_FMT = "%-I:%M %p"
    WEEKDAY_FMT = "%A"
    MONTH_FMT = "%b"
    YEAR_FMT = "%Y"
    DAY = "DAY"

    def __init__(self, booking: dict):
        # Booking metadata
        self.id = booking.get("id")
        self.book_id = booking.get("bookId")
        self.location_id = booking.get("lid")
        self.location_name = booking.get("location_name")
        self.space_id = booking.get("eid")
        self.space = booking.get("item_name")
        self.category_id = booking.get("cid")
        self.category_name = booking.get("category_name")
        self.status = booking.get("status")
        self.notes = booking.get("internal_notes")

        # Booking user info
        self.name = f"{booking.get('firstName')} {booking.get('lastName')}"
        self.email = booking.get("email")

        # Booking date info
        self.start = booking.get("fromDate")
        self.end = booking.get("toDate")
        self.start_time = self._get_datetimes(self.start, Booking.MINUTES_HOURS_FMT)
        self.end_time = self._get_datetimes(self.end, Booking.MINUTES_HOURS_FMT)
        self.weekday = self._get_datetimes(self.start, Booking.WEEKDAY_FMT)
        self.year = self._get_datetimes(self.start, Booking.YEAR_FMT)
        self.month = self._get_datetimes(self.start, Booking.MONTH_FMT)
        self.day = self._get_datetimes(self.start, Booking.DAY)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "space_id": self.space_id,
            "space": self.space,
            "start": self.start,
            "end": self.end,
            "notes": self.notes
        }

    def _get_datetimes(self, time, fmt):
        """Takes a string in isoformat and a strftime and returns the part of the string"""

        if time is not None:
            date = dt.datetime.fromisoformat(time)
            if fmt == "DAY":
                return date.day
            else:
                return date.strftime(fmt)
        else:
            return None

    def __repr__(self):
        return f"<Booking id: {self.id} {self.name} {self.start} {self.end}>"

    def __str__(self):
        return f"{self.location_name} reserved by {self.name} from {self.start} to {self.end}"

    def __len__(self):
        """Returns the duration of the booking in minutes"""

        start = dt.datetime.fromisoformat(self.start)
        end = dt.datetime.fromisoformat(self.end)
        seconds = int((end - start).total_seconds())
        return seconds // 60
