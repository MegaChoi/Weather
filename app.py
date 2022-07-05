import requests

api_key = 'edb33546896b6ad3e1d57b86d9c0c8db'

country_code = input("Enter your country: ")
city_name = input("Enter city: ")

weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

weather = weather_data.json()

print(weather_data.json())
# Status indicator 
if weather_data.status_code == 200:
    print('Weather bot is running')
else:
    print('Error: Cannot fetch URL')


