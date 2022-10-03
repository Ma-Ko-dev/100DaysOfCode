import os
import datetime as dt
import pandas as pd
import smtplib
import mail_details as md
from random import choice

MAILSERVER = "smtp.gmail.com"
TEMPLATE_DIR = "letter_templates/"

# read data
birthdays = pd.read_csv("data/birthdays.csv")
# set date
today = dt.datetime.today()


def send_birthday_mail(name: str, email: str):
    """Takes a random template from the template directory, opens it and replaces the placeholder with "name". Then
       sends an email to the email it got from the function call. Takes str name and str email as arguments, returns
       nothing."""
    template = choice(os.listdir(TEMPLATE_DIR))
    with open(f"{TEMPLATE_DIR}{template}", mode="r") as file:
        text = file.read().replace("[NAME]", name)

    with smtplib.SMTP(MAILSERVER) as connection:
        connection.starttls()
        connection.login(user=md.EMAIL, password=md.PASSWORD)
        connection.sendmail(from_addr=md.EMAIL,
                            to_addrs=email,
                            msg=f"Subject: Hey {name}! It's your Birthday!\n\n"
                                f"{text}")


def check_birthday(day: int, month: int):
    """Checks if today is a birthday of someone in our csv file. If so, it calls the send_birthday_mail with the name
       and email as argument. Takes int day and int month as"""
    bd = birthdays[(birthdays.day == day) & (birthdays.month == month)]
    if not bd.empty:
        name = bd.name.to_string(index=False)
        email = bd.email.to_string(index=False)
        send_birthday_mail(name, email)
    else:
        print("No Birthday today!")


check_birthday(day=today.day, month=today.month)
