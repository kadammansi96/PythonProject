import requests

MY_LAT = 18.638529
MY_LONG = 73.847786
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


# API Parameter

paramenter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 1,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramenter)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
