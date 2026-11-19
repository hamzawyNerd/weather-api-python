import requests
import os
from dotenv import load_dotenv
from weather import Weather

url = "https://api.weatherapi.com/v1/current.json"


# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    raise ValueError("API Key not found in .env")

print("API Key loaded successfully!")

params = {
    "key": api_key,
    "q": "Kafr El Sheikh"
}




try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Connection Error:", error)

else:
    city = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]

    weather = Weather(
        city,
        temperature,
        condition,
        humidity
    )

    weather.display_summary()

