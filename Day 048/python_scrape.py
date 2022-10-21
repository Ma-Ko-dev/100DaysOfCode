from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"E:\Dev-ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.python.org/")

try:
    event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
    event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
    events = {}

    for i in range(len(event_dates)):
        events[i] = {
            "time": event_dates[i].text,
            "name": event_names[i].text,
        }
    print(events)

finally:
    driver.quit()



#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last

#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1)