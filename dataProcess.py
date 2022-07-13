from cv2 import convexityDefects
import requests
import pycountry
import json
import random
from postTweet import Tweet
from countryinfo import CountryInfo
import keyboard
import time

class weather:

    def __innit__(self,city,country):
        self.city = city 
        self.country = country

    def getMeDaInfo(city,country):
        # get user input : country and city name  
        country_name = country
        city_name = city
        if country_name != None or country_name != "":
            country_code = pycountry.countries.get(name=country_name).alpha_2
        
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
            temperature = 'Temperature: ' + str(round(weather_data.json()['main']['temp'])) + '°' + ' C'
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
            
        elif weather_data.status_code == 400:
            print('----City Not Found----')
        else:
            print('----Error: Cannot fetch URL----')
        test = (country_name, city_name, temperature, clouds,humidity,wind)
        return test












