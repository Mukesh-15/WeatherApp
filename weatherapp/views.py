from django.shortcuts import render
from django.http import HttpResponse
import requests as rs
import datetime as dt
from .images import getImage

def home(request):
    CITY = "Hyderabad"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "1de43ba8c2da35df3eb169aa4b8840c0"
    
    if request.method == 'POST':
        CITY = (request.POST['city']).capitalize()
        image_url =getImage(CITY)

        url = BASE_URL + "appid="+API_KEY+"&q="+CITY
        res = rs.get(url).json()
        temp = str(int(res['main']['temp']-273))+"°"
        wind_speed=res['wind']['speed']
        pressure =res['main']['pressure']
        humidity =res['main']['humidity']
        description = res['weather'][0]['main']
        icon = res['weather'][0]['icon']
        return render(request,'weather_api.html',{
            'city':CITY,
            'temp':temp,
            'wind_speed':wind_speed,
            'pressure':pressure,
            'humidity':humidity,
            'description':description,
            'icon':icon,
            'image_url':image_url
            })
    
    url = BASE_URL + "appid="+API_KEY+"&q="+CITY
    res = rs.get(url).json()
    temp = str(int(res['main']['temp']-273))+"°"
    wind_speed=res['wind']['speed']
    pressure =res['main']['pressure']
    humidity =res['main']['humidity']
    description = res['weather'][0]['main']
    icon = res['weather'][0]['icon']
    image_url =getImage(CITY)
    return render(request,'weather_api.html',{
            'city':CITY,
            'temp':temp,
            'wind_speed':wind_speed,
            'pressure':pressure,
            'humidity':humidity,
            'description':description,
            'icon':icon,
            'image_url':image_url
            })