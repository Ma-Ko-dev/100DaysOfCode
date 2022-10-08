import requests
import smtplib
from credentials import *
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
YESTERDAY = str((datetime.today() - timedelta(days=1)).date())
BEFORE_YESTERDAY = str((datetime.today() - timedelta(days=2)).date())


def get_stock_info() -> tuple:
    payload = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API
    }
    response = requests.get(STOCK_ENDPOINT, params=payload)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    d1 = float(data[YESTERDAY]["4. close"])
    d2 = float(data[BEFORE_YESTERDAY]["4. close"])

    percentage_difference = round(abs((d1 - d2)) / ((d1 + d2) / 2) * 100, 4)

    symbol = ""
    if d2 > d1:
        symbol = "DOWN"
    elif d2 < d1:
        symbol = "UP"

    return percentage_difference, symbol


def get_news() -> list:
    payload = {
        "q": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": NEWS_API,
    }
    response = requests.get(NEWS_ENDPOINT, params=payload)
    response.raise_for_status()
    news_response = response.json()

    news_list = []
    for news in news_response["articles"]:
        news_list.append(f"HEADLINE: {news['title']}")
    return news_list


def send_email(stock_data: tuple) -> None:
    latest_news = get_news()
    symbol = stock_data[1]

    with smtplib.SMTP(MAILSERVER) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TARGET_MAIL,
                            msg=f"Subject: Stock Market report!\n\n"
                                f"TSLA: {symbol} -> {stock_data[0]}%\n"
                                f"{latest_news[0]}\n{latest_news[1]}\n{latest_news[2]}")


stock_difference = get_stock_info()
if stock_difference[0] >= 5:
    send_email(stock_difference)
