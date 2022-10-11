from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_IATA = "LON"

# sheet_data = DataManager().get_destination_data()
sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
# print(sheet_data)


for data in sheet_data:
    if data["iataCode"] == "":
        print(f"no data for {data['city']}")
        data["iataCode"] = FlightSearch().get_destination_code(data['city'])
    else:
        print(f"Data found for {data['city']} -> {data['iataCode']}")
# print(sheet_data)

# DataManager().update_iata_code(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
in_six_months = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = FlightSearch().check_flights(
        ORIGIN_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=in_six_months
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        print(f"Low price alert for {flight.destination_city}!\nSending E-mail...")
