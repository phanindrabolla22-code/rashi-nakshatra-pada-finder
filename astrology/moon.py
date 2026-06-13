import swisseph as swe
import pytz
from datetime import datetime


def get_sidereal_moon_longitude(
    year,
    month,
    day,
    hour,
    minute,
    timezone_name
):
    local_tz = pytz.timezone(timezone_name)

    local_dt = local_tz.localize(
        datetime(
            year,
            month,
            day,
            hour,
            minute
        )
    )

    utc_dt = local_dt.astimezone(
        pytz.utc
    )

    utc_hour = (
        utc_dt.hour
        + utc_dt.minute / 60
        + utc_dt.second / 3600
    )

    swe.set_sid_mode(swe.SIDM_LAHIRI)

    jd = swe.julday(
        utc_dt.year,
        utc_dt.month,
        utc_dt.day,
        utc_hour
    )

    moon = swe.calc_ut(
        jd,
        swe.MOON,
        swe.FLG_SIDEREAL
    )

    return moon[0][0]