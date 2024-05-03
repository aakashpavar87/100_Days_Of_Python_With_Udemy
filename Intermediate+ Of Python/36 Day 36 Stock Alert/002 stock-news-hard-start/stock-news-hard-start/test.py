import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# https://newsapi.org/v2/everything?apiKey=0bbbe6a5ae9241328a8e8338d9467cfe&qInTitle='Tesla Inc'&searchIn=title,content
params = {
    "apiKey": "0bbbe6a5ae9241328a8e8338d9467cfe",
    "qInTitle": COMPANY_NAME,
    "searchIn": "title,content"
}
response = requests.get(url=NEWS_ENDPOINT, params=params)
response.raise_for_status()
news_data = response.json()["articles"]
my_articles = news_data[:3]
# print(my_articles)
my_articles_msg = [f"Headline : {article['title']}. \nBrief : {article['description']}" for article in my_articles]
print(my_articles_msg)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference
# between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    # HINT 1: Think about using the Python Slice Operator
