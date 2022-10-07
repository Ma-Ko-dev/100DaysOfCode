import requests
import smtplib
from credentials import *


URL = "https://api.openweathermap.org/data/2.5/onecall"


def send_mail_notification() -> None:
    """Sends an email notification to alert the user of rain."""
    with smtplib.SMTP(MAILSERVER) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TARGET_MAIL,
                            msg=f"Subject: It will rain today!\n\n"
                                f"Dont forget to bring an umbrella today because it will rain!")


payload = {
    "lat": LATI,
    "lon": LONG,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(URL, params=payload)
response.raise_for_status()

data = response.json()["hourly"][:12]
for i in data:
    if i["weather"][0]["id"] < 700:
        # if the code is lower than 700 it rains or snows. we then print a message and call the mail function
        # after that, we break out of the loop
        print("It will rain in the next 12 hours, bring an Umbrella.")
        send_mail_notification()
        break
