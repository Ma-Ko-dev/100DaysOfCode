from credentials import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import time


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        self.driver.implicitly_wait(20)

        try:
            # clicking the "allow cookies" thing
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div > button._a9--._a9_1'))).click()
        except NoSuchElementException:
            print("cookie click not found")

        try:
            # finding and filling the email field
            email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
            email.send_keys(INSTA_ACC)
        except NoSuchElementException:
            print("login field not found")

        try:
            # finding and filling password field
            password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(INSTA_PW)
        except NoSuchElementException:
            print("PW field not found")

        try:
            # clicking login
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()
        except NoSuchElementException:
            print("login btn not found")

        try:
            # denie to save login
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'main > div > div > div > div > button'))).click()
        except NoSuchElementException:
            print("dont save login btn not found")

        try:
            # denie to alerts
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div > div > div._a9-z > button._a9--._a9_1'))).click()
        except NoSuchElementException:
            print("alert denied popup not found")

    def find_followers(self):
        url = f"https://www.instagram.com/{SIMILAR_ACC}/"
        self.driver.get(url)
        self.driver.implicitly_wait(20)

        try:
            # click the follower count
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'section > ul > li:nth-child(2) > a > div'))).click()
        except NoSuchElementException:
            print("no follower link found")

    def follow(self):
        try:
            # click the follow button
            for i in range(1, 5 + 1):
                delay = random.randint(2, 6)
                time.sleep(delay)
                WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 f'/html/body/div[1]/div/div/div/'
                                                                                 f'div[2]/div/div/div[1]/div/div[2]/'
                                                                                 f'div/div/div/div/div[2]/div/div/'
                                                                                 f'div[2]/div[2]/div/div[{i}]/div[3]/'
                                                                                 f'button/div/div'))).click()
                """
                For some clarification: This program will only follow the first 5 people that follow account xyz.
                I stopped at this point to prove that its possible to follow people automatically. The Script has to
                do a few more things to be really considered a follower bot. First thing would be searching for more 
                than 5 follow buttons to click. Then it has to scroll to find more people and lastly there needs to be 
                a way to handle the possibility that the script clicks on someone that it already followed and instagram
                now asks if i really want to unfollow. This is all possible, but not in my interest. I only wanted to
                prove it is possible and that i can do it.
                """

        except NoSuchElementException:
            print("follower btn not found")
        finally:
            time.sleep(15)
            self.driver.quit()


if __name__ == "__main__":
    instagram = InstaFollower()
    instagram.login()
    instagram.find_followers()
    instagram.follow()
