import requests
import os
import json

"""
    http://openweathermap.org
"""

OWM_API_KEY = os.environ.get('OPENWEATHERMAP_KEY')
KELVIN = -273.15


class Weather():

    def getWeather(self, city):
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWM_API_KEY)).json()
        temp = float(response["main"]["temp"]) + KELVIN
        return round(temp,2)
