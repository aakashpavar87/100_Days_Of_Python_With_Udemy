import requests
from twilio.rest import Client
import os

account_sid = "ACbb2c35cad3e71842e62ae828e8736a04"
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")

OPEN_WEATHER_MAP_URL = "https://api.openweathermap.org/data/3.0/onecall"
OPEN_WEATHER_KEY = os.environ.get("OWM_API_KEY")
print(auth_token, OPEN_WEATHER_KEY)
params = {
    "lat": 13.072090,
    "lon": 80.201859,
    "exclude": "minutely,daily",
    "appid": OPEN_WEATHER_KEY
}
response = requests.get(url=OPEN_WEATHER_MAP_URL, params=params)
response.raise_for_status()
content = response.json()["hourly"][:12]

for cn in content:
    weather_id = cn["weather"][0]["id"]
    if weather_id < 600:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+14159685399',
            body='Carry an ☂️ Umbrella it going to rain today ',
            to='+916351771513'
        )
        print(message.status)
        break
    else:
        print(f"Weather ID : {weather_id} Sunny")
