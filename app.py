from fastapi import FastAPI
import requests

app = FastAPI()

def meteorologie(api_key, ville):
    openWeatherUrl = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"
    info = requests.get(openWeatherUrl)
    meteo = info.json()

    if meteo["cod"] == 200:
        infoGeneral = meteo["main"]
        infoMeto = meteo["weather"][0]
        temperature = infoGeneral["temp"]
        description = infoMeto["description"]
        return f"La météo dans la vile de {ville} est {description} avec une température de {temperature} degré Celsius."
    else:
        return "La ville que vous chercher est introuvable."
    
@app.get("/")
def home():
    return {"message": "Bienvenu dans weather app!"}

@app.get("/about")
def about():
    return {"message": "WeatherApp est une application qui permet de voir les prévisions météorologique d'une ville."}

@app.get("/meteo/{ville}")
def meteo_par_ville(ville: str):
    api_key = open('secret.txt', 'r').read()
    result = meteorologie(api_key, ville)
    return {"ville": ville, "Metéo": result}