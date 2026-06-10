# import requests

MY_LAT= 5.603717
MY_LNG= -0.186964

# response= requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()["iss_position"]["longitude"]

# longitude=response.json()["iss_position"]["longitude"]
# latitude=response.json()["iss_position"]["latitude"]

# iss_position=(longitude,latitude)

# print(iss_position)

import requests
from datetime import datetime

parameters={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data= response.json()
sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now=datetime.now()
print(time_now.hour)