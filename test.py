import json 
import pycountry
from countryinfo import CountryInfo 
import random
import time
import requests
api_key = 'edb33546896b6ad3e1d57b86d9c0c8db'
i = 0
while True:
    try:
        list = json.load(open('data.json'))
        random_country_num = list[i]
        i = i + 1
        country_info = pycountry.countries.get(numeric= random_country_num )
    except IndexError:
        i = 0
        
    try:
        capital = CountryInfo(country_info.name).capital()
        country_code = country_info.alpha_2
    except KeyError:
        continue
    print(country_code, "****", capital)
    time.sleep(0.1)

    weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={capital + ',' + country_code}&units=metric&APPID={api_key}")

    # see raw data
    weather = weather_data.json()
    print(weather_data.json())