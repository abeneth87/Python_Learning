from selenium import webdriver
from selenium.webdriver.common.by import By

#Keeping chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

events_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text,
    }

print(events)