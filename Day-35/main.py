import requests
import json
from twilio.rest import Client
api_key= "your api key"
account_sid= "your account token"
auth_token= "you twilio account token"

lat= 28.704060
lon= 77.102493

parameters= {
    "lat": 45.070339,
    "lon":7.686864,
    "appid": "your openweather api key",
    "units": "metric",
    "cnt":4
}

response= requests.get(url= "https://api.openweathermap.org/data/2.5/forecast",params= parameters)
response.raise_for_status()
weather_data= response.json()
data= weather_data["list"]

will_rain= False
for item in data:
    id= item["weather"][0]["id"]
    if int(id)<700:
        will_rain= True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Its going to rain today,Bring An Umbrella☂️.",
    from_="your twilio number",
    to="the number you want to send the message"
    )

    print(message.status)
