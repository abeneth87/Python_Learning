import requests
from tabulate import tabulate

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "API_KEY"
NEWS_API_KEY = "NEWS_API"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,

}
print(f"Let us see {COMPANY_NAME} stocks!")
print("---------------------------------")
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(f"Yesterday's Closing Price: {yesterday_closing_price:.2f}")

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(f"Day Before Yesterday's Closing Price:{day_before_yesterday_closing_price}")

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(f"Price Difference: {difference:.2f}")

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(f"2 day difference percentage: {diff_percent:.2f}%")

#If percentage is greater than 5 then print("Get News").
if diff_percent > 4:
    print("Get News.....")
    #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    new_params ={
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]
    # get the first 3 news pieces for the COMPANY_NAME.
    three_articles = articles[:3]
    table_data = []
    for article in three_articles:
        headline = article['title']
        brief = article['description']
        table_data.append([headline, brief])

    # Format the table using tabulate.
    table = tabulate(table_data, headers=["Headline", "Brief"], tablefmt="grid")

    # Print the formatted table.
    print(table)




