import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL="testertont351@gmail.com"
MY_PASSWORD="adabrakadabra"

MY_LAT = 25.603717 # Your latitude
MY_LONG = -0.186964 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def ISSClose(my_lat,my_long,iss_lat,iss_long):
    lat=False
    long=False
    if my_lat - 5 <= iss_lat <= my_lat + 5:
        lat = True
    if my_long - 5 <= iss_long <= my_long + 5:
        long = True
    return (lat and long)




parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(datetime.now().hour)


#If the ISS is close to my current position
# and it is currently dark
def CurrentlyDark(sunrise,sunset,current_hour):
    
    if sunrise>=current_hour>=sunset:
        return(True)
    else:
        return(False)


def sendEmail(currentlyDark,issClose):
    if currentlyDark and issClose:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆🏼\n\n The ISS is above you in the sky"
        )
        

while True:
    time.sleep(60)
    sendEmail(
        currentlyDark=CurrentlyDark(sunrise=sunrise,sunset=sunset,current_hour=time_now),
        issClose=ISSClose(my_lat=MY_LAT,
                my_long=MY_LONG,
                iss_lat=iss_latitude,
                iss_long=iss_longitude))
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



