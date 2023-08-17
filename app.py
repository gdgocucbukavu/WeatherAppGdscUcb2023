from fastapi import FastAPI
from getweather import meteo,previsions

print("hello everyone")
api_key = "1fceafa4d5469574428c00f485b0b738"
app = FastAPI()

@app.get("/")
def read_route():
    return {"hello":"marie"}

@app.get("/meteo/{ville}")
def envoidata(ville:str):
    return (meteo(ville,api_key))

@app.get("/previsions/{ville}")
def envoidata(ville:str):
    return(previsions(ville,api_key))



    
