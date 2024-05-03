import requests
param = {
    "Authorization": "Basic bG9yZGFha2FzaDpBYWthc2hAODc="
}
URL = "https://api.sheety.co/99d049e611336755b6d90147fe881378/flightDeals/prices"
code = ["BER", "SYD", "KUL", "SFO", "KWI"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=URL, headers=param)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()




# for i in range(1, 6):
#     self.response = requests.put(url=f"{URL}/{i+1}",
#                                  json={"price": {"iataCode": code[i-1]}},
#                                  headers=param)
    # self.response = requests.delete(url=f"{URL}/{i}", headers=param)
# myData = DataManager()
# print()
