import requests
from datetime import datetime
from credentials import *


def get_exercise_data() -> list:
    user_input = input("Tell me which exercises you did: ").lower()

    headers = {
        "x-app-id": NUTRI_APP_ID,
        "x-app-key": NUTRI_APP_KEY,
        "Content-Type": "application/json",
    }

    body = {
        "query": user_input,
        "gender": NUTRI_GENDER,
        "weight_kg": NUTRI_WEIGHT,
        "height_cm": NUTRI_HEIGHT,
        "age": NUTRI_AGE,
    }

    response = requests.post(NUTRI_EXERCISE_EP, json=body, headers=headers)
    response.raise_for_status()
    data = response.json()["exercises"]
    return data


def add_for_exercise() -> None:
    nutri_data = get_exercise_data()
    date_today = datetime.today().strftime("%d/%m/%Y")
    time_today = datetime.now().strftime("%H:%M:%S")

    for workout in nutri_data:
        headers = {
            "Authorization": SHEEPY_AUTH,
            "Content-Type": "application/json",
        }

        body = {
            "workout": {
                "date": date_today,
                "time": time_today,
                "exercise": workout["name"].title(),
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],
            }
        }

        response = requests.post(SHEETY_EP, json=body, headers=headers)
        response.raise_for_status()


if __name__ == "__main__":
    add_for_exercise()
