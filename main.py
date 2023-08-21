import datetime as dt
import requests

openWeatherUrl = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('secret.txt', 'r').read()
ville = input("Entrez le nom de la ville: ")

def conversionDegres(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

urlComplet = f"{openWeatherUrl}appid={API_KEY}&q={ville}"
resultat = requests.get(urlComplet).json()

temperatureKelvin = resultat['main']['temp']
temperatureCelsius, temperatureFahrenheit = conversionDegres(temperatureKelvin)
feels_like_kelvin = resultat['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = conversionDegres(feels_like_kelvin)
vitesseVent = resultat['wind']['speed']
humidite = resultat['main']['humidity']
description = resultat['weather'][0]['description']
leverSoleil = dt.datetime.utcfromtimestamp(resultat['sys']['sunrise'] + resultat['timezone'])
coucherSoleil = dt.datetime.utcfromtimestamp(resultat['sys']['sunset'] + resultat['timezone'])

print(f"La température dans {ville} est de: {temperatureCelsius:.2f}°C ou {temperatureFahrenheit:.2f}°F")
print(f"La température dans {ville} se resent à: {feels_like_celsius:.2f}°C ou {feels_like_fahrenheit:.2f}°F")
print(f"L'humidité dans {ville} est de: {humidite}%")
print(f"La vitesse du vent dans {ville} est de: {vitesseVent} m/s")
print(f"La météo générale dans {ville} est: {description}")
print(f"L'heure du lever de soleil dans {ville} est: {leverSoleil} heure locale")
print(f"L'heure du coucher de soleil dans {ville} est: {coucherSoleil} heure locale")