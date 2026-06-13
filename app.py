import streamlit as st
from datetime import datetime

from astrology.location import get_location_details
from astrology.moon import get_sidereal_moon_longitude
from astrology.real_nakshatra import get_nakshatra_and_pada
from astrology.rashi import get_rashi
from astrology.lagna import get_lagna


st.set_page_config(
    page_title="Rashi, Nakshatra & Pada Finder",
    page_icon="🔮",
    layout="centered"
)

st.title("🔮 Rashi, Nakshatra & Pada Finder")
st.markdown(
    "Enter your birth details to calculate **Rashi**, **Nakshatra**, **Pada**, and **Lagna**."
)

# Inputs
dob = st.text_input(
    "Date of Birth (DD-MM-YYYY)",
    placeholder="please enter your date of birth in DD-MM-YYYY format"
)

birth_time = st.text_input(
    "Birth Time (HH:MM - 24 Hour Format)",
    placeholder="please enter your birth time in HH:MM format"
)

place = st.text_input(
    "Birth Place",
    placeholder="please enter your birth place"
)

if st.button("Find Details"):

    if not dob or not birth_time or not place:
        st.error("Please fill all fields.")
        st.stop()

    try:
        # Parse date
        date_obj = datetime.strptime(
            dob,
            "%d-%m-%Y"
        )

        # Parse time
        hour, minute = map(
            int,
            birth_time.split(":")
        )

        # Get location details
        latitude, longitude, timezone = get_location_details(
            place
        )

        # Lagna
        lagna_sign, lagna_degree = get_lagna(
            date_obj.year,
            date_obj.month,
            date_obj.day,
            hour,
            minute,
            timezone,
            latitude,
            longitude
        )

        # Moon longitude
        moon_longitude = get_sidereal_moon_longitude(
            date_obj.year,
            date_obj.month,
            date_obj.day,
            hour,
            minute,
            timezone
        )

        # Nakshatra & Pada
        nakshatra, pada = get_nakshatra_and_pada(
            moon_longitude
        )

        # Rashi
        rashi = get_rashi(
            moon_longitude
        )

        st.success("Calculation Completed")

        st.divider()

        st.subheader("📋 Birth Details")

        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**Birth Time:** {birth_time}")
        st.write(f"**Birth Place:** {place}")

        st.divider()

        st.subheader("📍 Location Information")

        st.write(f"**Latitude:** {latitude}")
        st.write(f"**Longitude:** {longitude}")
        st.write(f"**Timezone:** {timezone}")

        st.divider()

        st.subheader("🌙 Astrology Results")

        st.write(f"**Moon Longitude:** {round(moon_longitude, 4)}°")
        st.write(f"**Nakshatra:** {nakshatra}")
        st.write(f"**Pada:** {pada}")
        st.write(f"**Rashi:** {rashi}")

        st.divider()

        st.subheader("⭐ Lagna")

        st.write(f"**Lagna (Ascendant):** {lagna_sign}")
        st.write(f"**Lagna Degree:** {round(lagna_degree, 4)}°")

    except ValueError:
        st.error(
            "Invalid Date or Time format. Use DD-MM-YYYY and HH:MM."
        )

    except Exception as e:
        st.error(f"Error: {e}")