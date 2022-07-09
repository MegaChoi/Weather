import requests
import pycountry
from postTweet import Tweet



# get user input : country and city name  
country_name = input("Enter your country: ").title()
if country_name != None or country_name != "":
    country_code = pycountry.countries.get(name=country_name).alpha_2
city_name = input("Enter city: ").title()

# get data back in the form of json file
api_key = 'edb33546896b6ad3e1d57b86d9c0c8db'
weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={city_name + ',' + country_code}&units=metric&APPID={api_key}")

# see raw data
weather = weather_data.json()
# print(weather_data.json())

# Status indicator 
if weather_data.status_code == 200:
    print('----The weather bot is running----')
    #temp
    temperature = 'Temperature: ' + str(round(weather_data.json()['main']['temp'])) + '°'
    print(temperature)
    #clouds
    clouds = weather_data.json()['weather'][0]['main'] + ", " + weather_data.json()['weather'][0]['description']
    print(clouds)
    #humidity
    humidity = 'Humidity:' + str(weather_data.json()['main']['humidity']) + '%'
    print(humidity)
    #windspeed 
    wind = 'Wind Speed:'+ str(weather_data.json()['wind']['speed']) + "m/s"
    print(wind)
    # calling post method if only status code is == 200
    Tweet.postTweet(city_name, temperature, clouds,humidity,wind)
    
elif weather_data.status_code == 400:
    print('----City Not Found----')
else:
    print('----Error: Cannot fetch URL----')











