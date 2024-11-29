#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = 'censored, re-add your key here'

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:])
url = 'http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=3&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()
lonlatData = json.loads(response.text)
lat = lonlatData[0]['lat']
lon = lonlatData[0]['lon']
url2 = 'https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s' % (lat, lon, APPID)
response2 = requests.get(url2)
response2.raise_for_status()
weatherData = json.loads(response2.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
