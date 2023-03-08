import requests
import os


API_KEY = os.getenv("OPEN_WEATHER")


def get_weather_data(city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # API returns in 3 hrs so to get 24...
    num_of_values = 8 * days
    filtered_data = filtered_data[0:num_of_values]
    return filtered_data


