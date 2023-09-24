import requests
MY_LAT = 12.988444
MY_LONG = 80.259047
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "API_KEY_DUMMY"

weather_params ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]
#slicing only the 12 hour from the list of 60 hours
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella")

