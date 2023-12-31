from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
import os
from bs4 import BeautifulSoup

# CHANGE ME
ZILLOW_LINK = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfqdDrE6sfvxkN4BhVBfjz98Itd6XfJzA-RWrEtbgoMfzS6Tw/viewform?usp=sf_link"

sel_path = os.path.join(os.getcwd(), 'selenium')
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=" + sel_path)
options.add_argument("user-data-dir=selenium")

ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfqdDrE6sfvxkN4BhVBfjz98Itd6XfJzA-RWrEtbgoMfzS6Tw/viewform?usp=sf_link"

headers = {
    'accept': 'text/html,application/html+xml,application/xml;q=0.9,image/webp,image/apng,*/*q=0.8',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


class ZillowScrapper:
    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def go_zillow(self):
        with requests.Session() as session:
            response = session.get(ZILLOW_URL, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            prices = soup.find_all(
                attrs={"data-test": "property-card-price"})
            property_prices = []
            for price in prices:
                p = int(price.text.split()[0].replace(
                    "$", "").replace(",", "").replace("+", "").replace("/mo", ""))
                property_prices.append(p)

            addresses = soup.find_all(
                attrs={"data-test": "property-card-addr"})
            property_addresses = []
            for address in addresses:
                property_addresses.append(address.text)

            urls = soup.find_all(
                attrs={"data-test": "property-card-link"})
            property_urls = []
            for url in urls:
                if 'http' in url['href']:
                    property_urls.append(url['href'])
                else:
                    property_urls.append(
                        'https://www.zillow.com' + url['href'])

            self.go_form(property_prices, property_addresses, property_urls)

    def go_form(self, prices, addresses, urls):
        self.driver.get(FORM_URL)
        time.sleep(2)
        for i in range(len(prices)):
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(addresses[i])
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(prices[i])
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(urls[i])
            self.driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
            time.sleep(1)
            self.driver.find_element(
                By.XPATH, '//a[text()="Enviar otra respuesta"]').click()
            time.sleep(2)
            print(i)


bot = ZillowScrapper()
bot.go_zillow()
