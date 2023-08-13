import requests
import json

api_key = "1fceafa4d5469574428c00f485b0b738"


def meteo(city_name,api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    return data
def previsions(city_name,api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    return data