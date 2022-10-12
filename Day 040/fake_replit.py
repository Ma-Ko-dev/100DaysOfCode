import requests
from credentials import *


def add_user(firstName, lastName, mail):
    headers = {
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": firstName,
            "lastName": lastName,
            "email": mail
        }
    }

    response = requests.post(url=SHEETY_EP_USER, headers=headers, json=body)
    response.raise_for_status()


print("Welcome to Gariot's Flight Club.")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()
email = input("What is your email?\n")
email_check = input("Type your email again.\n")

if email == email_check:
    print("You are in the club!")
    # add_user(first_name, last_name, email)
else:
    print("Your emails didn't match, please try again by refreshing.")
