# 🌌 ISS Overhead Notifier
# This program checks if the International Space Station (ISS) is currently
# near your location and if it’s dark outside. If both conditions are true,
# it sends you an email notification so you can look up and try to spot the ISS.

import requests
from datetime import datetime
import smtplib
import time

# =======================
# ✅ User Configuration
# =======================

MY_LAT = -42.4377          # *Your latitude*
MY_LONG = 179.4578        # *Your longitude*

MY_EMAIL = "avinashnegi1999temp@gmail.com"      # *Sender email*
MY_PASSWORD = "znrivdixpkrrnchi"               # *Gmail App Password*
TO_EMAIL = "avinashnegi1999temp@gmail.com"     # *Receiver email*

# =======================
# 🔭 Function Definitions
# =======================

def is_iss_overhead():
    """
    *Check if ISS is close to your location.*
    Returns True if ISS is within ±5 degrees of latitude and longitude.
    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # ! Stop if API request fails
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # ✅ Return True if ISS is near your location
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


def is_night():
    """
    *Check if it is currently dark at your location.*
    Uses the Sunrise-Sunset API (UTC time).
    Returns True if current UTC hour is after sunset or before sunrise.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # ! 0 = ISO time format (returns UTC)
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # ? Extract sunrise and sunset hours (in UTC)
    sunrise_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # ? Get current UTC hour
    current_utc_time = datetime.utcnow()
    time_now = current_utc_time.hour

    # ✅ Return True if it is dark (after sunset or before sunrise)
    return time_now >= sunset_utc or time_now <= sunrise_utc


def send_email():
    """
    *Send an email notification.*
    Informs the user that the ISS is overhead.
    """
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # ! Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky!"
        )

# =======================
# ⏱ Main Loop
# =======================
# *Check every 60 seconds if ISS is overhead and it’s dark.*
while True:
    time.sleep(60)  # *Pause for 60 seconds between checks*
    if is_iss_overhead() and is_night():
        send_email()  # *Send email notification*
