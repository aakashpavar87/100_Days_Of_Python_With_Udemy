import smtplib

import requests
from datetime import datetime

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude

MY_LAT = 23.022505
MY_LONG = 72.571365
MY_PASS = "cwdfzwgskdqvquwf"
MY_MAIL = "aakashpavar87@gmail.com"


def is_iss_above_me():
    my_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    my_response.raise_for_status()
    my_data = my_response.json()
    iss_latitude = float(my_data["iss_position"]["latitude"])
    iss_longitude = float(my_data["iss_position"]["longitude"])
    min_lat = MY_LAT - 5
    max_lat = MY_LAT + 5
    min_lng = MY_LONG - 5
    max_lng = MY_LONG + 5
    return ((iss_latitude <= max_lat) or (iss_latitude >= min_lat)) and ((iss_longitude <= max_lng) or (iss_longitude >= min_lng))


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return (time_now >= sunset or time_now < sunrise)

if is_iss_above_me() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject: ISS Position"
                                                                     "\n\nLook out ISS is above you.")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



