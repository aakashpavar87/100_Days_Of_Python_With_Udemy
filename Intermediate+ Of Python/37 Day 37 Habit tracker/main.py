import datetime

import requests

PIXELA_URL = "https://pixe.la"
USER_ENDPOINT = "%s/v1/users" % PIXELA_URL
GRAPH_ENDPOINT = "%s/v1/users/lordaakash7/graphs" % PIXELA_URL
get_graph_url = "%s/v1/users/lordaakash7/graphs/codinggraph7.html" % PIXELA_URL
POST_VALUE_GRAPH_URL = "%s/v1/users/lordaakash7/graphs/codinggraph7" % PIXELA_URL
TOKEN = "a7wQgKzAkvQXPBq"
user_config = {
    "token": TOKEN,
    "username": "lordaakash7",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": "codinggraph7",
    "name": "Coding Habit",
    "unit": "Hrs",
    "type": "int",
    "color": "ichou"
}
today = datetime.datetime(year=2023, month=11, day=25)
dt = today.strftime("%Y%m%d")
value_config = {
    "date": dt,
    "quantity": "4"
}
PUT_DATA_URL = f"{PIXELA_URL}/v1/users/lordaakash7/graphs/codinggraph7/{dt}"
update_value_config = {
    "quantity": "3",
    # "optionalData": {
    #     "unit": "Hrs"
    # }
}
DELETE_DATA_URL = f"{PIXELA_URL}/v1/users/lordaakash7/graphs/codinggraph7/{dt}"
# print(PUT_DATA_URL)
# response = requests.post(url=USER_ENDPOINT, json=user_config)
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# response = requests.post(url=POST_VALUE_GRAPH_URL, json=value_config, headers=headers)
# response = requests.put(url=PUT_DATA_URL, json=update_value_config, headers=headers)
response = requests.delete(url=DELETE_DATA_URL, headers=headers)
response.raise_for_status()
print(response.text)
