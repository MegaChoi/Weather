import requests
import pycountry
api_key = 'edb33546896b6ad3e1d57b86d9c0c8db'

country_name = input("Enter your country: ").title()
country_code = pycountry.countries.get(name=country_name).alpha_2
city_name = input("Enter city: ").title()

# get data back in the form of json file
weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={city_name + ',' + country_code}&units=metric&APPID={api_key}")

# see raw data
weather = weather_data.json()
print(weather_data.json())

# Status indicator 
if weather_data.status_code == 200:
    print('----The weather bot is running----')
elif weather_data.status_code == 200:
    print('----City Not Found----')
else:
    print('----Error: Cannot fetch URL----')

#temp
print('Temperature: ', round(weather_data.json()['main']['temp']),'°')
#clouds
print(weather_data.json()['weather'][0]['main'] + ", " + weather_data.json()['weather'][0]['description'])
#humidity
print('Humidity:', weather_data.json()['main']['humidity'],'%')
#windspeed 
print('Wind Speed:', weather_data.json()['wind']['speed'], "m/s")
