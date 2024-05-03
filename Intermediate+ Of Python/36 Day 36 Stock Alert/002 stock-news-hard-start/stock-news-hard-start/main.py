import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": "Z96QR31WFB9HFVKG"
}

response = requests.get(url=STOCK_ENDPOINT, params=params)
response.raise_for_status()
up_down = None
stock_data = response.json()["Time Series (Daily)"]
my_data = [value for key, value in stock_data.items()]
yesterday_close_price = float(my_data[0]["4. close"])
day_before_close_price = float(my_data[1]["4. close"])
price_difference = yesterday_close_price - day_before_close_price
percentage_diff = (abs(price_difference) / yesterday_close_price) * 100
if price_difference < 0:
    up_down = "🔻"
else:
    up_down = "🔺"
my_articles = None
if percentage_diff > 0.4:
    params = {
        "apiKey": "0bbbe6a5ae9241328a8e8338d9467cfe",
        "q": COMPANY_NAME
    }
    response = requests.get(url=NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    news_data = response.json()["articles"]
    my_articles = news_data[:3]
    print(my_articles)

my_articles_msg = [f"Headline : {article['title']} {STOCK} {up_down}. \nBrief : {article['description']}" for article in my_articles]
account_sid = "ACbb2c35cad3e71842e62ae828e8736a04"
auth_token = os.environ.get("AUTH_TOKEN_TWILIO")

for msg in my_articles_msg:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+14159685399',
        body=msg,
        to='+916351771513'
    )

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
