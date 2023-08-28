# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import urllib
import time
import random

w = "800"
h = "1280"
email = ''
password = ''
username = ''
r_sleep10 = time.sleep(random.randint(5,10))
r_sleep5 = time.sleep(random.randint(3,5))

useragent = random.choice(['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.13 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'])


def main():
    isprofile = os.path.isdir(os.path.join(os.getcwd(), 'profile'))
    bot = Tweetbot(email, password ,username)
    if not isprofile:
        print("not profile")
        bot.login()

    time.sleep(random.randint(10,15))

   # bot.update_status_with_media('image',['image1.png'])

class Tweetbot:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("--disable-infobars")
        options.add_argument("--window-size=" + h + "x" + w)
        options.add_argument("--no-sandbox")
        options.add_argument("disable-blink-features=AutomationControlled")
        options.add_argument("--lang=ja-JP")
        options.add_argument("--hide-scrollbars")
        options.add_argument("--enable-gpu")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
#        options.add_argument("--single-process")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--user-agent=" + useragent)
        options.add_argument("--user-data-dir=%s" % os.path.join(os.getcwd(), 'profile'))
        options.add_argument("--profile-directory=Default")
        print("--user-data-dir=%s" % os.path.join(os.getcwd(), 'profile'))

        self.driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=options)
        self.driver.set_window_size(w,h)

        self.driver.implicitly_wait(random.randint(10,14))

    def login(self):
        driver = self.driver
        driver.get('https://twitter.com/i/flow/login')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username'")))
        r_sleep5
        driver.save_screenshot('debug-log.png')

        try:
            elm = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
            driver.save_screenshot('debug-login1.png')
            elm.send_keys(self.email)
            elm.send_keys(Keys.RETURN)
            print(u"ユーザーネームを入力")
            r_sleep5
        except:
            print(u"ユーザーネーム失敗")
            driver.save_screenshot('debug-login.png')
            pass

        try:
            elm = driver.find_element(By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
            elm.send_keys(self.username)
            elm.send_keys(Keys.RETURN)
            print(u"メアド入力")
            r_sleep5
        except:
            driver.save_screenshot('debug-username.png')
            print(u"メアド失敗")
            pass

        try:
            elm = driver.find_element(By.XPATH, "//input[@name='password']")
            elm.send_keys(self.password)
            elm.send_keys(Keys.RETURN)
            r_sleep5
            r_sleep10
            print(u"パスワード")
        except:
            driver.save_screenshot('debug_password.png')
            print(u"パスワード失敗")
            pass


if __name__ == "__main__":
    main()

