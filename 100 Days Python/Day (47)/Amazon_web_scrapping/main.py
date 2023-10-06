from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    #Try running this code only once every few minutes, Running often will result in CAPTCHA generation link

    # Extract Product Title
    title = soup.find("span", {"id": 'productTitle'}).get_text(strip=True)

    # Extract Product Price as a float
    price_text = soup.find('span', class_='a-price').find('span', class_='a-offscreen').text.strip().replace('$', '')
    price = float(price_text)

    print("Product Title =", title)
    print("Product Price =", price)
