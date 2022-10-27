import time
import requests
import validators
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from credentials import *


class DataEntry:
    def __init__(self):
        self.zillow = "https://www.zillow.com/"
        self.link_list = []
        self.price_list = []
        self.address_list = []
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                          "Version/14.0.2 Safari/605.1.15",
            "Accept-Language": "en-US"
        }
        data = requests.get(ZILLOW_SEARCH, headers=headers).text
        self.bs = BeautifulSoup(data, "html.parser")

    def get_links(self):
        entries_raw = self.bs.select("div.result-list-container > ul > li > article > div > div > a")
        for entry in entries_raw:
            if validators.url(entry['href']):
                self.link_list.append(entry['href'])
            else:
                self.link_list.append(f"{self.zillow}{entry['href']}")

    def get_prices(self):
        prices_raw = self.bs.select("div.result-list-container > ul > li > article > div > div > div > span")
        for price in prices_raw:
            if "+" in price.text:
                self.price_list.append(price.text.split("+")[0])
            elif "/" in price.text:
                self.price_list.append(price.text.split("/")[0])

    def get_addresses(self):
        address_raw = self.bs.select("div.result-list-container > ul > li > article > div > div > a")
        for address in address_raw:
            self.address_list.append(address.text)

    def enter_data(self):
        for i in range(len(self.address_list)):
            self.driver.get(GOOGLE_FORM)
            self.driver.implicitly_wait(20)

            try:
                address = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                address.send_keys(self.address_list[i])
            except NoSuchElementException:
                print("Address field not found")

            try:
                price = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                price.send_keys(self.price_list[i])
            except NoSuchElementException:
                print("Price field not found")

            try:
                link = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
                link.send_keys(self.link_list[i])
            except NoSuchElementException:
                print("Link field not found")

            try:
                WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))).click()
            except NoSuchElementException:
                print("Send Button not found")
            time.sleep(3)

        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    de = DataEntry()
    de.get_links()
    de.get_prices()
    de.get_addresses()
    de.enter_data()
