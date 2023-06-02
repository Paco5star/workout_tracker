import requests
from datetime import datetime
import os

APP_ID = "55c941d1"
API_KEY = "a4c3b39875452dbd7e66452dabd603ed"

gender = "male"
weight = 140
height = 176
age = 25
action_text = input("what excercise's did you do today")
sheety_endpoint = "https://api.sheety.co/ec24eea8ff35b9266a24e8fade5d7e84/workoutTracker/workouts"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
   "query": action_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
response = requests.post(endpoint, json=parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    date = datetime.now().strftime("%m/%d/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    headers = {
        "Authorization": f"bearer paco916"
    }
    add_row_endpoint = f"{sheety_endpoint}"
    add_row_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=add_row_endpoint, json=add_row_params, headers=headers)
    response.raise_for_status()



