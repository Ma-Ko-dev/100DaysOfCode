import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from credentials import *


URL = "https://www.linkedin.com/jobs/search/?currentJobId=3318944127&f_AL=true&geoId=101282230&keywords=python%20entwickler&location=Deutschland&refresh=true"

chrome_driver_path = r"E:\Dev-ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(URL)
time.sleep(2)

login_btn_initial = driver.find_element(By.LINK_TEXT, 'Einloggen')
login_btn_initial.click()
time.sleep(2)

login_mail = driver.find_element(By.NAME, 'session_key')
login_mail.send_keys(MAIL)
login_pw = driver.find_element(By.NAME, 'session_password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.ENTER)
time.sleep(5)

listings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')
# for loop to save ALL jobs
listings[0].click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.jobs-save-button').click()

# For now, the program just saves the first job in the list and then exits. It would be easy to loop through all jobs
# and save them or even send them an application.


# just some time before we quit to have time to see if something happened
time.sleep(5)
driver.quit()
