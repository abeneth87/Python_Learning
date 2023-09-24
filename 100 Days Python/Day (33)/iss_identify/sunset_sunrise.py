from datetime import datetime

import requests
MY_LAT = 12.988444
MY_LONG = 80.259047
parameters ={
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
