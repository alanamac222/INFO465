import requests

#url='https://api.open-meteo.com/v1/forecast' 

#response=requests.get(url,
                      #params={"latitude":37.5,
                      #"longitude":-77.46,
                      #"current":"temperature_2m"}) #Data Dictionary
#data=response.json()
#print(data.keys())
#print(data["current"]["temperature_2m"])



air_quality_url="https://air-quality-api.open-meteo.com/v1/air-quality"

response2=requests.get(air_quality_url,
                      params={"latitude":37.5,
                      "longitude":-77.46,
                      "current":"pm2_5"}) #Data Dictionary
data2=response2.json()
print(data2.keys())
print(data2["current"]["pm2_5"])