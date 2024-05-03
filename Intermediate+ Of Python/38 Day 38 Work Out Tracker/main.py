from datetime import datetime
import requests
import os

NUTRITIONIX_API_KEY = os.environ.get("APP_KEY")

NUTRITIONIX_APP_ID = os.environ.get("APP_ID")
WEB_ENDPOINT = "https://trackapi.nutritionix.com"
var = os.getenv("MY_VAR")
EXERCISE_ENDPOINT = "/v2/natural/exercise"

SHEETY_PASS = os.getenv("SHEETY_PASS")

HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}
params = {
    "query": input("Enter your excersize details : ")
}
exercise_url = f"{WEB_ENDPOINT}{EXERCISE_ENDPOINT}"
response = requests.post(url=exercise_url, json=params, headers=HEADERS)
data_list = response.json()["exercises"]

today = datetime.now()
date = f"{today.day}/{today.month}/{today.year}"
time = f"{today.hour}:{today.minute}:{today.second}"
exercise = ""
calories = 0
duration = 0
for data in data_list:
    exercise += f"{data['name'].title()} "
    duration += data['duration_min']
    calories += round(data['nf_calories'], 0)


POST_URL = "https://api.sheety.co/99d049e611336755b6d90147fe881378"
WORK_OUT_ENDPOINT = "/workoutTracker/workouts"
AUTHENTICATION = {
    "Authorization": f"Basic {SHEETY_PASS}"
}
work_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
response = requests.post(url=f"{POST_URL}{WORK_OUT_ENDPOINT}", json=work_params, headers=AUTHENTICATION)
print(response.text)
