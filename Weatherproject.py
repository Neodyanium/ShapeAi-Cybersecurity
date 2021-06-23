import requests
import json
from datetime import datetime

api_key = 'b30fe1773f672b9d88a7743786db48a3'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()



#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
def Create_file():
    f = open('data','w')
    f.write("""
    -------------------------------------------------------------
    Weather Stats for - {}  || {}
    ------------------------------------------------------------
    Current temperature  = {}
    Current weather desc = {}
    Current Humidity     = {}
    Current wind speed   = {}
    """.format(location.upper(),date_time,temp_city,weather_desc,hmdt,wind_spd))
    print ("-------------------------------------------------------------")
    print("The Current weather data was saved successfully")
    print ("-------------------------------------------------------------")


# The Create_file is declared will replicate the same into data file
Create_file()

# using json module replicate the data sent by API (RAW). I tried didn't find a way to process data.
with open('data.txt','w') as file:
   file.write(json.dumps(api_data))
















