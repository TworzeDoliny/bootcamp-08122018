# import requests
# resp = requests.get("https://www.metaweather.com/api/location/search/?query=Warsaw")
# resp1 = requests.get("https://www.metaweather.com/api/location/523920/")
#
# pogoda = resp.json()[0]
# pogoda1 = resp1.json()
#
#
# print(pogoda)
# print(pogoda1)

import sys
import requests
from collections import namedtuple

localization = sys.argv[1]

Weather = namedtuple("Weather", ['location', 'temperature', 'air_pressure', 'humidity'])

def get_location_id(localization):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
    location_id = resp.json()[0]['woeid']
    return location_id

def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    resp_json = resp.json()['consolidated_weather'][0]

    weather = Weather(
        location=resp.json()['title'],
        temperature=resp.json()['the_temp'],
        air_pressure=resp.json()['air_pressure'],
        humidity=resp.json()['humidity']
    )

    return weather


def print_weather(weather):
    print(f"Pogoda w lokalizacji: {weather.location}"),
    print("Temperatura: ", weather.temperature)
    print("Ciśnienie powietrza: ", weather.air_pressure)
    print("Wilgotność: ", weather.humidity)

location_id = get_location_id(localization)
weather = get_location_weather(location_id)
print_weather(weather)
