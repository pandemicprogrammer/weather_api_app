# Weather API app
# MValentonis 3/9/2022

import requests
import csv
from keys import API_KEY


CITY = 'Shanghai'
COUNTRY = 'CN'
UNITS = 'imperial'

res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY},&units={UNITS}&appid={API_KEY}')
data = res.json()

print(data)

weather = data['weather'][0]['main']
temp = data['main']['temp']
wind_speed = data['wind']['speed']

header = ['city', 'country_code', 'weather', 'wind_speed', 'temp'] #CSV header columns
info = [CITY, COUNTRY, wind_speed, weather, temp]

with open('weather.csv', 'w') as f:
    #create csv
    writer = csv.writer(f)
    #writes header row
    writer.writerow(header)
    #writes info row
    writer.writerow(info)

