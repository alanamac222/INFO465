import requests

def fetch_data(lat=37.55,lon=-77.46):
    """This function takes a lat long and returns temp and air quality"""

    url1= "https://api.open-meteo.com/v1/forecast"
    url2 = "https://air-quality-api.open-meteo.com/v1/air-quality"

    response=requests.get(
        url1,
        params={
            "latitude":lat,
            "longitude":lon,
            "current":"temperature_2m"

            }) 
    data=response.json()
    temperature=data["current"]["temperature_2m"]

    response2=requests.get(
        url2,
        params={
            "latitude":lat,
            "longitude":lon,
            "current":"pm2_5"

            }) 
    data2=response2.json()
    pm2_5=data2["current"]["pm2_5"]

    return {
        "temperature":temperature,
        "pm2_5":pm2_5, "lat":lat, "lon":lon
    }

if __name__=="__main__":
    print(fetch_data())