import requests
import os
from datetime import datetime



pixeLa_endpoint= "https://pixe.la/v1/users"
token= os.getenv("token")
username= os.getenv("username")

parameters={
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response= requests.post(url= pixeLa_endpoint,json= parameters)
# print(response.text)

graph_endpoint= f"{pixeLa_endpoint}/{username}/graphs"
graph_config= {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "minute",
    "type": "float",
    "color": "ajisai"
}

headers={
    "X-USER-TOKEN": token
}
# response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
today= datetime.now()

graphPixel_endpoint=  f"{pixeLa_endpoint}/{username}/graphs/graph1"
pixelConfig= {
    "date":today.strftime("%Y%m%d"),
    "quantity":"60",
}

# response= requests.post(url=graphPixel_endpoint,json=pixelConfig,headers=headers)
# print(response.text)
pixelUpdate_endpoint=f"{pixeLa_endpoint}/{username}/graphs/graph1/20260415"
pixelUpdate={
    "quantity": "45",

}
# response= requests.put(url= pixelUpdate_endpoint,json=pixelUpdate,headers=headers)
# print(response.text)

deletePixel_endpoint=f"{pixeLa_endpoint}/{username}/graphs/graph1/20260415"
# response= requests.delete(url=deletePixel_endpoint,headers=headers)