import swisseph as swe
import pytz
from datetime import datetime


RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def get_lagna(year, month, day, hour, minute, timezone, latitude, longitude):

    # 1. Local time
    local_tz = pytz.timezone(timezone)
    local_dt = local_tz.localize(datetime(year, month, day, hour, minute))

    # 2. Convert to UTC (IMPORTANT STEP)
    utc_dt = local_dt.astimezone(pytz.utc)

    # 3. Convert to decimal UT hour
    ut_hour = utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600

    # 4. Julian Day (UTC based)
    jd = swe.julday(
        utc_dt.year,
        utc_dt.month,
        utc_dt.day,
        ut_hour
    )

    # 5. Houses (Placidus system)
    houses, ascmc = swe.houses(jd, latitude, longitude)

    asc = ascmc[0]

    sign_index = int(asc // 30)

    return RASHIS[sign_index], asc