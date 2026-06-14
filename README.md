# 🔮 Rashi, Nakshatra & Pada Finder

A Python-based Vedic Astrology application that calculates **Rashi (Moon Sign)**, **Nakshatra (Birth Star)**, **Pada**, and **Lagna (Ascendant)** from a user's birth details.

The application uses **Swiss Ephemeris** for accurate astronomical calculations and automatically detects location coordinates and timezone from the birth place.

## Features

- Calculate Moon Rashi
- Find Nakshatra
- Determine Nakshatra Pada
- Calculate Lagna (Ascendant)
- Automatic Latitude & Longitude Detection
- Automatic Timezone Detection
- Streamlit Web Interface

## Tech Stack

- Python
- Streamlit
- Swiss Ephemeris (pyswisseph)
- Geopy
- TimezoneFinder
- Pytz

## Project Workflow

```text
Birth Details
      ↓
Location Detection
      ↓
Timezone Conversion
      ↓
Moon Longitude Calculation
      ↓
Rashi + Nakshatra + Pada
      ↓
Lagna Calculation
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Sample Output

```text
Nakshatra : Mrigashira
Pada      : 2
Rashi     : Taurus
Lagna     : Cancer
```

## Future Improvements

- Planetary Positions
- Birth Chart (Kundli)
- Vimshottari Dasha
- PDF Report Generation

## Author

**Phanindra Bolla**
