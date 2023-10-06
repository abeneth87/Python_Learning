from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import *

#Keeping chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# wiki_pages = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(f"The total number of articles in Wikipedia: {wiki_pages.text} ")

search = driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

while(True):
       pass

