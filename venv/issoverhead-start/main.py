import requests
from datetime import datetime
import pandas
import smtplib
import time


my_gmail = "russnicosia.auto@gmail.com"
my_gmail_password = "cmibneqfnjiclvnm"
MY_LAT = 15.56 # Your latitude
MY_LONG = 125.99 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.
if (MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5) and (MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5):
    with smtplib.SMTP("smtp.gmail.com", 587) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(user=my_gmail, password=my_gmail_password)
        gmail_connection.sendmail(
            from_addr=my_gmail,
            to_addrs="russnicosia@gmail.com",
            msg=f"Subject: !!!!!! ISS SPACE STATION IS ABOVE YOU !!!!!!\n\nThe ISS Space station is close by above you. If it is night time go take a look!\n\n- Automated Russ"
        )

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

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



