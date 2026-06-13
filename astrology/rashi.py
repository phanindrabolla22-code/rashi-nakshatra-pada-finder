RASHIS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]

def get_rashi(longitude):
    index = int(longitude // 30)

    if index > 11:
        index = 11

    return RASHIS[index]