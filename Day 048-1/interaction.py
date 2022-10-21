import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"E:\Dev-ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://secure-retreat-92358.herokuapp.com/")

try:
    fname = driver.find_element(By.NAME, 'fName')
    fname.send_keys("Gariot")
    lname = driver.find_element(By.NAME, 'lName')
    lname.send_keys("Grau")
    email = driver.find_element(By.NAME, 'email')
    email.send_keys("max.mustermann@web.de")
    btn = driver.find_element(By.TAG_NAME, 'button')
    btn.click()
    # just a short sleep so i can see the results :D
    time.sleep(3)
finally:
    driver.quit()
