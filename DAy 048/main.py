import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"E:\Dev-ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]


def show_coockie_per_second():
    print(driver.find_element(By.ID, 'cps').text)


def set_pricelist():
    upgrade_prices = []
    upgrades = driver.find_elements(By.CSS_SELECTOR, '#store b')
    for price in upgrades:
        if price.text != "":
            cost = int(price.text.split("-")[1].strip().replace(",", ""))
            upgrade_prices.append(cost)
    return upgrade_prices


def set_upgrades(upgrade_prices):
    cookie_upgrades = {}
    for n in range(len(upgrade_prices)):
        cookie_upgrades[upgrade_prices[n]] = item_ids[n]
    return cookie_upgrades


def get_money():
    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",", "")
    return int(money)


def buy_upgrades():
    upgrade_prices = set_pricelist()
    cookie_upgrades = set_upgrades(upgrade_prices)
    cookie_count = get_money()

    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_upgrades[cost] = id

    highest_price_affordable_upgrade = max(affordable_upgrades)
    to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

    driver.find_element(By.ID, to_purchase_id).click()


def click_cookie():
    timeout = time.time() + 5
    game_over = time.time() + 60 * 5

    while True:
        if time.time() > game_over:
            print("Times Up.")
            break
        elif time.time() > timeout:
            print("Checking for Upgrades.")
            buy_upgrades()
            timeout = time.time() + 5
        else:
            cookie.click()
    print("Show Coockies per second")
    show_coockie_per_second()


if __name__ == "__main__":
    click_cookie()
    print("Quiting Browser...")
    driver.quit()
