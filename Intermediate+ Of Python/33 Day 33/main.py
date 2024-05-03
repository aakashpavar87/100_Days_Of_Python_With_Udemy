import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# address = (data['iss_position']['latitude'], data['iss_position']['longitude'])
# print(address)
ahmedabad_params = {
    "lat": 23.022505,
    "lng": 72.571365,
    "formatted": 0
}
london_params = {
    "lat": 51.507351,
    "lng": -0.127758
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=london_params)
ahm_response = requests.get(url="https://api.sunrise-sunset.org/json", params=ahmedabad_params)
response.raise_for_status()
# print(response.json())
# print(ahm_response.json())
ahm_sunset = ahm_response.json()["results"]["sunset"].split("T")[1].split(":")
ahm_sunrise = ahm_response.json()["results"]["sunrise"].split("T")[1].split(":")

time_now = datetime.now()

sunrise = ahm_sunrise[0]
sunset = ahm_sunset[0]
print(sunrise, sunset, time_now.hour)
