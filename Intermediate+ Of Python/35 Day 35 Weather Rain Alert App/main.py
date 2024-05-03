import requests
from twilio.rest import Client
# API_KEY = "d46e76f16f0df7166af18cd1c0ed0daa"
# WEATHERSTACK_API_KEY = "5942677436a2970999b8b1c81370cd88"
# WEATHERBIT_API_KEY = "e5ae730783334fadbbe3a8f718e94ab7"
# http://api.openweathermap.org/geo/1.0/direct?q=Ahmedabad,India&limit=5&appid=43f197b07e99833b4544198d140aaefb
# http://api.openweathermap.org/data/2.5/weather?q=Ahmedabad,Gujarat&appid=43f197b07e99833b4544198d140aaefb
# WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
# ONE_CALL_URL = "https://api.openweathermap.org/data/2.5/onecall"
# WEATHERSTACK_URL = "https://api.weatherstack.com/current"
# WEATHERBIT_URL = "https://api.weatherbit.io/v2.0/forecast/daily"
# WEATHER_KEY = "7a67bbdfbe7c407d9cea846ac575d335"
# params = {
#     "q": "Ahmedabad,Gujarat",
#     "appid": API_KEY
# }
# https://api.openweathermap.org/data/3.0/onecall?lat=23.022505&lon=72.571365&exclude=minutely,daily&appid=720e039f21abb3460d49bcc6eb4ce6cd

account_sid = 'ACbb2c35cad3e71842e62ae828e8736a04'
auth_token = '6ff9656f00aa9059d28545d5923bcc05'

OPEN_WEATHER_MAP_URL = "https://api.openweathermap.org/data/3.0/onecall"
OPEN_WEATHER_KEY = "720e039f21abb3460d49bcc6eb4ce6cd"

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
            body='Carry an ☂️ Umbrella it gonna rain today ',
            to='+916351771513'
        )
        print(message.status)
        break
    else:
        print(f"Weather ID : {weather_id} Sunny")
# print(content)
