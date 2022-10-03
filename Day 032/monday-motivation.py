from random import choice
import datetime as dt
import smtplib
import mail_details as md
# mail_details not included in GitHub

MAILSERVER = "smtp.gmail.com"
QUOTE_FILE = "data/quotes.txt"

# working with isoweekday() here. 1 = Monday, ..., 7 = Sunday
target_day = 1
current_day = dt.datetime.today().isoweekday()


def send_monday_mail():
    with open(QUOTE_FILE, mode="r") as file:
        data = file.readlines()
        rand_quote = choice(data)

    with smtplib.SMTP(MAILSERVER) as connection:
        connection.starttls()
        connection.login(user=md.EMAIL, password=md.PASSWORD)
        connection.sendmail(from_addr=md.EMAIL,
                            to_addrs=md.TARGET_MAIL,
                            msg=f"Subject:Here is your Monday motivation E-Mail!\n\n"
                                f"{rand_quote}")


if current_day == target_day:
    print("Today is the day!")
    send_monday_mail()
else:
    print("We better wait a little bit more.")

