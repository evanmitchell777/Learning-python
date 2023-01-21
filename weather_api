#weather app
import requests 
import json
location=input("enter city name here: ")
url='http://api.weatherapi.com/v1/current.json?key=042421b17e574278825231804232001 &q={0}&aqi=no'.format(location.title())
response = requests.get(url)
data = json.loads(response.text)
location=data['current']
temp=location['temp_f']
print (temp)
