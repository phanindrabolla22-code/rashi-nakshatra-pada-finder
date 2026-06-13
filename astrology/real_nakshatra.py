NAKSHATRAS = [
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashira",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati"
]

def get_nakshatra(sidereal_longitude):
    nak_span = 360 / 27

    index = int(sidereal_longitude // nak_span)

    if index >= 27:
        index = 26

    return NAKSHATRAS[index]


def get_nakshatra_and_pada(sidereal_longitude):
    nak_span = 360 / 27
    pada_span = nak_span / 4

    nak_index = int(sidereal_longitude // nak_span)

    if nak_index >= 27:
        nak_index = 26

    remainder = sidereal_longitude % nak_span

    pada = int(remainder // pada_span) + 1

    if pada > 4:
        pada = 4

    return NAKSHATRAS[nak_index], pada