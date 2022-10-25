from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import *
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speed_url = "https://www.speedtest.net/"
        self.driver.get(speed_url)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/'
                                           'span[4]').click()
        time.sleep(70)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                           'div[8]/div/a').click()
        time.sleep(3)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/'
                                                       'span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                     'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"My Downloadspeed is: {self.down}")
        print(f"My Uploadspeed is: {self.up}")
        time.sleep(5)

    def tweet_at_provider(self):
        twitter_url = "https://twitter.com/"
        self.driver.get(twitter_url)
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/'
                                               'div[3]/div[5]/a/div/span/span').click()
            time.sleep(2)
        except NoSuchElementException:
            print("login btn not found")

        try:
            login_mail = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                            'div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/'
                                                            'div/div[2]/div/input')
            login_mail.send_keys(TWITTER_EMAIL)
            login_mail.send_keys(Keys.ENTER)
            time.sleep(2)
        except NoSuchElementException:
            print("email field not found")

        try:
            login_pw = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                          'div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/'
                                                          'div[2]/div[1]/input')
            login_pw.send_keys(TWITTER_PASSWORD)
            login_pw.send_keys(Keys.ENTER)
        except NoSuchElementException:
            login_pw = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                          'div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/'
                                                          'div/input')
            login_pw.send_keys(TWITTER_USER)
            login_pw.send_keys(Keys.ENTER)
            time.sleep(3)
            login_pw = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                          'div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/'
                                                          'div[2]/div[1]/input')
            login_pw.send_keys(TWITTER_PASSWORD)
            login_pw.send_keys(Keys.ENTER)
            time.sleep(5)

        try:
            tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/'
                                                           'div[1]/div[3]/a/div')
            tweet_btn.click()
        except NoSuchElementException:
            print("btn not found")

        time.sleep(5)
        try:
            tweet_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                             'div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/'
                                                             'div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/'
                                                             'label/div[1]/div/div/div/div/div/div[2]/div')
            tweet = f"My Internetspeed today is: {self.down} Down and {self.up} Up!"
            tweet_field.send_keys(tweet)
            time.sleep(5)
        except NoSuchElementException:
            print("tweet box not found")

        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/'
                                               'div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/'
                                               'span/span').click()
            time.sleep(5)
        except NoSuchElementException:
            print("send btn not found")
        finally:
            self.driver.quit()


twot = InternetSpeedTwitterBot()
twot.get_internet_speed()
twot.tweet_at_provider()
