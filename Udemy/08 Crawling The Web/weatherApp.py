import re

from urllib import request

#http://www.weather-forecast.com/locations/Nakuru/forecasts/latest

city = input("Enter city: ")

url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data = request.urlopen(url).read().decode('utf-8')