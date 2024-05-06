from fastapi import FastAPI


from getweather import meteo, previsions, api_key




app = FastAPI()


# GET method in FastAPI
@app.get("/")
def get_information():
    return {"message": "This is the information you requested"}

#get weather
@app.get("/weather/{city_name}")
def get_weather(city_name: str):
    return meteo(city_name,api_key)

#get weather forecast
@app.get("/forecast/{city_name}")
def get_forecast(city_name: str):

    return previsions(city_name,api_key)
# Run the app with uvicorn
# uvicorn app:app --reload