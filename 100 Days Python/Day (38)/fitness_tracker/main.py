import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 79
HEIGHT_CM = 183
AGE = 35

APP_ID = "KEY"
API_KEY = "KEY"

natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/{CODE}/workoutTracking/workouts"

exercise_text = input("What exercise did you do today? ")

params = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=natural_language_endpoint, json=params, headers=headers)
result = response.json()

# print(result)
#----Sheety Integration----#

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%x")

for exercise in result["exercises"]:
    sheet_inputs ={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)

    # sheet_response = requests.post(
    #     url=sheety_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #             "user_name",
    #             "Password",
    #     )
    # )
