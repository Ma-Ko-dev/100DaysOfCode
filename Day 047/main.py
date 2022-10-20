import requests
import smtplib
import mail_details as md
from bs4 import BeautifulSoup


def send_mail_notification(current_price, title, url):
    with smtplib.SMTP(md.MAILSERVER) as connection:
        connection.starttls()
        connection.login(user=md.EMAIL, password=md.PASSWORD)
        connection.sendmail(from_addr=md.EMAIL, to_addrs=md.TARGET_MAIL,
                            msg=f"Subject: Amazon Price alert!\n\n"
                                f"Price alert for:\n{title}\n"
                                f"Current price is {current_price:.2f}€!\n"
                                f"Check it out at:\n{url}")


def check_price(current_price, title, url):
    target_price = 28.99
    if current_price <= target_price:
        send_mail_notification(current_price, title, url)


def get_current_price():
    product_url = "https://www.amazon.de/dp/B07XD4PPMX/?th=1&psc=1"

    headers = {
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/106.0.0.0 Safari/537.36",
    }

    response = requests.get(product_url, headers=headers)
    response.raise_for_status()
    data = response.text

    bs = BeautifulSoup(data, "lxml")
    price = float(bs.select_one("span.a-offscreen").text.replace("€", "").replace(",", "."))
    title = bs.find("title").text
    check_price(price, title, product_url)


if __name__ == "__main__":
    get_current_price()
