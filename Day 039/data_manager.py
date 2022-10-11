from credentials import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_destination_data(self):
        headers = {
            "Authorization": SHEETY_AUTH,
            "Content-Type": "application/json",
        }

        response = requests.get(url=SHEETY_EP)
        response.raise_for_status()
        return response.json()["prices"]


    def update_iata_code(self, cities):
        for city in cities:
            new_code = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_EP}/{city['id']}",
                                    json=new_code)
            print(response.text)
