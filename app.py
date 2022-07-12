import requests
import pycountry
import json
import random
from postTweet import Tweet
from countryinfo import CountryInfo
import keyboard
import time
# get user input : country and city name  
# country_name = input("Enter your country: ").title()
# if country_name != None or country_name != "":
#     country_code = pycountry.countries.get(name=country_name).alpha_2
# city_name = input("Enter city: ").title()


#fully automated program without needing the terminal input
i = 0
while i != 10:
    #get country info 
    try:
        list = json.load(open('data.json'))
        random_country_num = list[i]
        i = i + 1
        country_info = pycountry.countries.get(numeric= random_country_num )
    except IndexError:
        i = 0
    #get capital, name and alpha 2 code 
    try:
        country_name = country_info.name
        capital = CountryInfo(country_name).capital()
        country_code = country_info.alpha_2
    except KeyError:
        continue
    print(country_code, "****", capital)


    # get data back in the form of json file
    api_key = 'edb33546896b6ad3e1d57b86d9c0c8db'
    weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={capital + ',' + country_code}&units=metric&APPID={api_key}")

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
        Tweet.postTweet(country_name, capital, temperature, clouds,humidity,wind)
        
    elif weather_data.status_code == 400:
        print('----City Not Found----')
    else:
        print('----Error: Cannot fetch URL----')
    time.sleep(300)











