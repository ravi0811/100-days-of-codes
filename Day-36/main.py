import os
import requests







STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key= os.getenv("API")


parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response= requests.get(url=STOCK_ENDPOINT,params= parameter)
response.raise_for_status()

data= response.json()
time_series = data["Time Series (Daily)"]
data_list= [value for (key,value) in time_series.items()]
yesterday_data= data_list[0]
yesterday_closing_price= yesterday_data["4. close"]


day_before_yesterday= data_list[1]
day_before_yesterday_closing_price= day_before_yesterday["4. close"]

difference= abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))

diff_percent= (difference/float(yesterday_closing_price))*100 
news_apiKey= os.getenv("news_api")
if diff_percent>5:
    news_params={
        "apiKey": news_apiKey,
        "q":COMPANY_NAME
    }
    news_response= requests.get(NEWS_ENDPOINT,params= news_params)
    articles= news_response.json()["articles"]
    

    three_articles= articles[:3]


formatted_articles=[f"Headline: {article['title']}. \nBrief: {article['description']}"for article in three_articles]
print(formatted_articles)

for article in formatted_articles:
    print(article+"\n\n\n")