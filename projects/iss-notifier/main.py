# Application programming interface is a set of commands, functions, protocols and objects
# to create software or interact with external systems

# 1XX : Hold On
# 2XX : Here You Go
# 3XX : Go Away
# 4XX : Request Screwed Up
# 5XX : Server Screwed Up

import requests
from datetime import datetime
import smtplib
import time
import os

my_email = "nishant.guvvada@gmail.com"
password = os.getenv('PASSWORD')

MY_LAT = 28.570845
MY_LONG = 77.212250

def iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()["iss_position"]
    iss_lat = float(iss_data["latitude"])
    iss_long = float(iss_data["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    data = sunrise_response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[1])
    sunset = int(data["sunset"].split("T")[1].split(":")[1])

    current_time = datetime.now().hour

    if current_time >= sunset or current_time <= sunrise:
        return True

    print(sunrise)
    print(sunset)
    print(current_time)

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:LOOK UPy\n\nTHE ISS IS ABOVE YOU IN THE SKY!")