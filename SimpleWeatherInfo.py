
# Simple weather application written in Pythons
# This app using OpenWeather API. 
# If you want to use this app you have to sign up OpenWeather.
# And then you have to get API key to use in this app.
# https://openweathermap.org/appid
# My API key is  1234567890adefg9876543210dkslksd

# The "requests" module allows you to send HTTP requests using Python
# If this module not exist in your computer you have to download and install it, c:\> pip install requests
import requests

apiKey="384b75b1694084bf267035ca09f495a3"
webApiAddress="http://api.openweathermap.org/data/2.5/weather"
country="TR"
city="Antalya"
# This command sending request to api.openweathermap.org web address and getting JSON format data
# We requesting data using metric system "&units=Metric"
weatherInfo=requests.get(webApiAddress + '?q=' + city + ',' + country + '&units=Metric&appid=' + apiKey)
# If you don't want to use Metric System just delete "&units=Metric" and start to using Imperial System
# weatherInfo=requests.get(webApiAddress + '?q=' + city + ',' + country + '&appid=' + apiKey)

# print and show all weather data in JSON format
print(weatherInfo.json())
print("---------------------------------")
# Load JSON data-information to Dictionary and make it more useful to access
weatherDict=weatherInfo.json()
minTemp=weatherDict["main"]["temp_min"] # minimum temperature of the day
maxTemp=weatherDict["main"]["temp_max"] # maximum temperature of the day
humidity = weatherDict["main"]["humidity"] # humidity of the day

# in this section we using Dictionary to show data: country, city and all weather information
print(f'country : { weatherDict["sys"]["country"] }')
print(f'city : { weatherDict["name"] }')
# print(f'all temperature and humidity info : { weatherDict["main"] }')

# in this section we using variables to show data: maximum temp, minimum temp and humidity
print("maximum temperature : ", maxTemp)
print("minimum temperature : ", minTemp) 
print("humidity  : ", humidity ) 
