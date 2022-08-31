import requests
from datetime import datetime
import pandas
import smtplib
import time


my_gmail = "russnicosia.auto@gmail.com"
my_gmail_password = "cmibneqfnjiclvnm"
MY_LAT = 39.556975 # Your latitude
MY_LONG = -104.915242 # Your longitude
time_now = datetime.now()

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
is_running = True

while is_running:
    print(f"Current time is: {time_now}\nISS Space Station current coords are: {iss_latitude} "
          f"Latitude and {iss_longitude} Longitude\nYour home coords are: {MY_LAT} Latitude and "
          f"{MY_LONG} Longitude.")
    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5) and (MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5):
        print(f"Bro the ISS Space Station is really close by! YOu can probably see it in the sky if it is night time.\n"
              f"You'll get an email!")
        with smtplib.SMTP("smtp.gmail.com", 587) as gmail_connection:
            gmail_connection.starttls()
            gmail_connection.login(user=my_gmail, password=my_gmail_password)
            gmail_connection.sendmail(
                from_addr=my_gmail,
                to_addrs="russnicosia@gmail.com",
                msg=f"Subject: !!!!!! ISS SPACE STATION IS ABOVE YOU !!!!!!\n\nThe ISS Space station is close by above "
                    f"you. If it is night time go take a look!\n\n- Automated Russ"
            )
    else:
        pass
    time.sleep(60)

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

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



