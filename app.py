from fastapi import FastAPI
from getweather import meteo


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
def read_item(city: str):
    return meteo(city, "1fceafa4d5469574428c00f485b0b738")
