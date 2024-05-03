import requests
from datetime import timedelta
from datetime import datetime
import data_manager
TEQUILA_API_KEY = "4rK_19xZOG7au2mzYLTKUauclIV755FL"
TEQUILA_URL = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, dataManager : data_manager.DataManager):

        self.myfromdate = datetime.now().strftime("%d/%m/%Y")
        self.mytodate = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.data = dataManager
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.header = {
            "apikey": TEQUILA_API_KEY,
        }
        self.flight_data = []
        for cd in data_manager.code:
            self.params = {
                "fly_from": "AMD",
                "fly_to": cd,
                "date_from": self.myfromdate,
                "date_to": self.mytodate,
                "curr": "GBP"
            }
            self.response = requests.get(url=TEQUILA_URL, params=self.params, headers=self.header)
            self.response.raise_for_status()
            self.flight_data.append(round(self.response.json()["data"][0]["conversion"]["EUR"] * 0.86))
        self.cities = [city['city'] for city in self.data.sheet_data['prices']]
        for i in range(len(self.flight_data)):
            print(f"{self.cities[i]}: {self.flight_data[i]}")
#₹

myData = data_manager.DataManager()
ser = FlightSearch(myData)
# print(ser.flight_data)
