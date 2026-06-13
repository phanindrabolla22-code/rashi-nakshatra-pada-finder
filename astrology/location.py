from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from timezonefinder import TimezoneFinder
import time


def get_location_details(place):
    geolocator = Nominatim(user_agent="astrology_app", timeout=10)

    try:
        location = geolocator.geocode(place)

        # retry once if failed
        if location is None:
            time.sleep(1)
            location = geolocator.geocode(place)

        if location is None:
            raise ValueError(f"Place not found: {place}")

        latitude = location.latitude
        longitude = location.longitude

        tf = TimezoneFinder()
        timezone = tf.timezone_at(lat=latitude, lng=longitude)

        return latitude, longitude, timezone

    except (GeocoderTimedOut, GeocoderUnavailable):
        raise Exception("Location service is temporarily unavailable. Try again.")