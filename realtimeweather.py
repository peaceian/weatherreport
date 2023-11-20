from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
from json import loads
user_key = 'CWB-869C7631-CE97-4263-9AF8-635DF71E8A67'
doc_name = 'O-A0001-001'
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/%s?Authorization=%s" % (doc_name,user_key)
data = requests.get(url)
data_json = data.json()
locations = data_json['records']['Station']

"""
lat = []
lon = []
locationName = []
stationID = []
obsTime = []
ELE = []
WDIR = []
WDSD = []
TEMP = []
HUMD = []
PRES = []
WEATHER = []
CITY = []
TOWN = []
"""
for i in locations:
    lat = (i['GeoInfo']['Coordinates'][0]['StationLatitude'])
    lon = (i['GeoInfo']['Coordinates'][0]['StationLongitude'])
    StationName = (i['StationName'])
    StationId = (i['StationId'])
    obsTime = (i['ObsTime']['DateTime'])
    Altitude = (i['GeoInfo']['StationAltitude'])
    WDIR = (i['WeatherElement']['WindDirection'])
    WDSD = (i['WeatherElement']['WindSpeed'])
    TEMP = (i['WeatherElement']['AirTemperature'])
    HUMD = (i['WeatherElement']['RelativeHumidity'])# round(float x [, n]  )
    PRES = (i['WeatherElement']['AirPressure'])
    WEATHER = (i['WeatherElement']['Weather'])
    CITY = (i['GeoInfo']['CountyName'])
    TOWN = (i['GeoInfo']['TownName'])
    print(f'地名：{StationName} 城市：{CITY} 鄉鎮：{TOWN} 觀測站：{StationId} 氣象：{WEATHER} 觀測時間：{obsTime}\n')
    #print(f'高度：{Altitude} 風向：{WDIR} 風速：{WDSD} 溫度：{TEMP} 溼度：{HUMD} 緯度：{lat} 經度：{lon}\n')
