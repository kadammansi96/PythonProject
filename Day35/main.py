import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "89268cd35051918a6676b46896c635a1"
account_sid = "ACc58dd65805168f0b97c0af86d3cc3bac"
auth_token = "cff97c8c170ea8a052528b29ef5597ea"

parameters = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain, please carry your umbrella",
        from_='+12244902529',
        to='Your number',
    )

    print(message.status)