from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_iata_code()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}


tomorrow = datetime.now() + timedelta(days=1)
in_six_months = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=in_six_months
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                  f"{flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        # use notification manager here to send mails
