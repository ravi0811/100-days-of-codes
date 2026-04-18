import os
import requests
from datetime import datetime

now= datetime.now()

apiKey= os.getenv("APIKEY")
appId= os.getenv("APPID")
sheetyUrl= os.getenv("SHEETYURL")
nutriEndPoint=os.getenv("NUTRIENDPOINT")
auth= os.getenv("AUTH")
userName= os.getenv("USERNAME")
password= os.getenv("PASSWORD")


headers= {
    "x-app-id": appId,
    "x-app-key": apiKey
}


data={
    "query":"Exercise for 15 minutes",
    "date": now.date().strftime("%d/%m/%Y"), 
    "time": now.strftime("%H:%M:%S")
}

response= requests.post(url= nutriEndPoint,json=data,headers=headers)
response.raise_for_status()
result= response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheetyUrl,
        json=sheet_inputs,
        auth=(
            userName,
            password,
        )
    )

    print(sheet_response.text)