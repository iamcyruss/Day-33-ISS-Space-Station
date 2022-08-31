import requests
import datetime as dt

MY_LAT = 39.56
MY_LNG = -104.99
time_name = dt.datetime.now()
print(time_name)


"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]
longitude = data["longitude"]
latitude = data["latitude"]
iss_position = (latitude, longitude)
print(iss_position)
"""

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, )
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
