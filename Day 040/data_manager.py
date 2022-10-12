from credentials import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_EP)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_iata_code(self):
        for city in self.destination_data:
            new_code = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_EP}/{city['id']}",
                                    json=new_code)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_EP_USER
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
