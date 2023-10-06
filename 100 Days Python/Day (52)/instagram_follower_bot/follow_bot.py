from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

INSTA_USER = "user_name"
INSTA_PASS = "password"
SIMILAR_ACCT = "https://www.instagram.com/chefsteps"
INSTA_URL = "https://www.instagram.com/accounts/login/"
LOGIN_BTN_XPATH = '//*[@id="loginForm"]/div/div[3]/button/div'
FOLLOWERS_BTN_XPATH = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/" \
                      "header/section/ul/li[2]/a/div"


class InstaFollower:
    def __init__(self):
        self.driver = driver

    def login(self):
        # go to the instagram login page and wait 10 seconds (while the page loads)
        self.driver.get(INSTA_URL)
        time.sleep(10)
        # find the "username" field, type in the username and wait 5 seconds
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTA_USER)
        time.sleep(5)
        # find the "password" field, type in the password and wait 5 seconds
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTA_PASS)
        time.sleep(5)
        # find the login button, click it and wait 30 seconds (while the page loads)
        login_btn = self.driver.find_element(By.XPATH, LOGIN_BTN_XPATH)
        login_btn.click()
        time.sleep(30)

    def find_followers(self):
        # go to the selected instagram account that has the followers I want and wait 20 seconds
        self.driver.get(SIMILAR_ACCT)
        time.sleep(20)
        # click the followers link and wait 5 seconds
        followers_btn = self.driver.find_element(By.XPATH, FOLLOWERS_BTN_XPATH)
        followers_btn.click()
        time.sleep(5)
        # scroll down the followers list total height a total of 2 times and wait 5 seconds each time
        follower_list_scroll = self.driver.find_element(By.CSS_SELECTOR, "._aano")
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_list_scroll)
            time.sleep(5)

    def follow(self):
        # find all buttons using the CSS_SELECTOR, click on each one and wait 2 seconds each time
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._acan")
        # this is to test if list has elements in it or if it returns as empty (this took me many times to get right)
        print(all_buttons)
        follower_number = len(all_buttons)
        for num in range(1, follower_number):
            follower_button = self.driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div/div[2]/div/div/"
                                                                 f"div[1]/div/div[2]/div/div/div/div/div[2]/div/"
                                                                 f"div/div[2]/div[1]/div/div[{num}]/div[3]/button")
            follower_button.click()
            time.sleep(2)


bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()

