from selenium import webdriver
from selenium.webdriver.common.by import By

#Keeping chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/dp/B084884GKX/")

price_rupee = driver.find_element(By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
print(f"The price of the product is:{price_rupee.text} ")
