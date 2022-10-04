import time
import requests
from datetime import datetime

ISS_URL = "http://api.open-notify.org/iss-now.json"
SUN_URL = "https://api.sunrise-sunset.org/json"
MY_LATI = 35.467987
MY_LONG = 38.734802
# somewhere in Turkey. It was close when testing the code :D
MY_COORDS = {"lat": MY_LATI, "lng": MY_LONG}


def get_iss_coords():
    """Function returns the ISS position as dict (usable for the sunrise API) and returns nothing when it encounters
       an Error."""
    response = requests.get(url=ISS_URL)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as msg:
        print(f"Error: {msg}")
    else:
        iss_lat = response.json()["iss_position"]["latitude"]
        iss_lng = response.json()["iss_position"]["longitude"]
        iss_pos = {"lat": float(iss_lat), "lng": float(iss_lng)}
        return iss_pos


def get_sun_times(dict_coords: dict):
    """Returns the response from the sunrise API and handles errors when they should appear. Returns nothing if there
       is an error. Needs Latitude and Longitude in dictionary form as argument. See the Sunrise API for more
       details."""
    payload = dict_coords
    payload["formatted"] = "0"
    response = requests.get(SUN_URL, params=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as msg:
        print(f"Error: {msg}")
    else:
        return response.json()


def is_iss_close():
    """Returns bool+ if the ISS is close to MY_COORDS. Takes no arguments."""
    iss_lati, iss_long = get_iss_coords().values()
    time_now = datetime.now().strftime("%H:%M:%S")
    if MY_LATI - 5 <= iss_lati <= MY_LATI + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        print(f"{time_now}: ISS is close.")
        return True
    else:
        print(f"{time_now}: ISS is not close.")
        return False


def is_nighttime():
    """Returns a bool if its nighttime or not. Takes no arguments."""
    current_time = int(datetime.now().hour)
    sunrise = get_sun_times(MY_COORDS)["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = get_sun_times(MY_COORDS)["results"]["sunrise"].split("T")[1].split(":")[0]

    if current_time >= sunset or current_time <= sunrise:
        print("Its night time, look up!")
        return True
    else:
        print("But its daytime, you cant see the ISS!")
        return False


while True:
    # checking every minute for the ISS and if its nighttime
    time.sleep(60)
    if is_iss_close() and is_nighttime():
        print("Sending imaginary email...")
        # I just didn't want to get the email/password details again.






