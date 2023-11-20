import requests
import json
import math




user_key = 'CWB-869C7631-CE97-4263-8AF8-635DF71E8A67'
doc_name = 'O-A0001-001'
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/%s?Authorization=%s" % (doc_name,user_key)
data = requests.get(url)
data_json = data.json()
locations = data_json['records']['Station']
    
weather = {} #新增weather 字典

for i in locations:

    StationName = i['StationName']
    StationId = i['StationId']
    obsTime = i['ObsTime']['DateTime']
    lat = i['GeoInfo']['Coordinates'][0]['StationLatitude']
    lon = i['GeoInfo']['Coordinates'][0]['StationLongitude']
    Altitude = i['GeoInfo']['StationAltitude']
    CITY = i['GeoInfo']['CountyName']
    CoCode = i['GeoInfo']['CountyCode']
    TOWN = i['GeoInfo']['TownName']
    ToCode = i['GeoInfo']['TownCode']
    WEATHER = i['WeatherElement']['Weather']
    Precipitation = i['WeatherElement']['Now']['Precipitation']
    WDIR = i['WeatherElement']['WindDirection']
    WDSD = i['WeatherElement']['WindSpeed']
    TEMP = i['WeatherElement']['AirTemperature']
    HUMD = i['WeatherElement']['RelativeHumidity']
    PRES = i['WeatherElement']['AirPressure']
    PGS = i['WeatherElement']['GustInfo']['PeakGustSpeed']
    HXWDIR = i['WeatherElement']['GustInfo']['Occurred_at']['WindDirection']
    HXWDT = i['WeatherElement']['GustInfo']['Occurred_at']['DateTime']
    DXTEMP = i['WeatherElement']['DailyExtreme']['DailyHigh']['TemperatureInfo']['AirTemperature']
    DXTEMPT = i['WeatherElement']['DailyExtreme']['DailyHigh']['TemperatureInfo']['Occurred_at']['DateTime']
    DNTEMP = i['WeatherElement']['DailyExtreme']['DailyLow']['TemperatureInfo']['AirTemperature']
    DNTEMPT = i['WeatherElement']['DailyExtreme']['DailyLow']['TemperatureInfo']['Occurred_at']['DateTime']


    #weather作為一個空字典，將輸入的城市鄉鎮保留，[CITY]=[a],[locationName]=[b]
    msg = f'{TEMP}度，{WEATHER}，相對濕度{HUMD}%，累積雨量{Precipitation}mm，觀測時間{obsTime}' #天氣描述
    try:
        weather[CITY][StationName] = msg #紀錄地區和描述  #CITY跟TOWN同層，選一種當搜尋字
    except:
        weather[CITY] = {} #如果每個縣市不是字典，建立第二層字典
        weather[CITY][StationName] = msg 
    
show = ''
for i in weather:
    show = show + i + ',' #列出可輸入的縣市名稱
show = show.strip(',') #移除結尾逗號
a = input(f'請輸入下方其中一個縣市\n{show}\n') #使用者輸入縣市名稱 #a = input({show})

show = ''
for i in weather[a]: #weather[a]裡尋找
    show = show + i + ',' #列出可輸入的地點名稱
show = show.strip(',') #移除結尾逗號
b = input(f'請輸入{a}的其中一個地點\n{show}\n') #使用者輸入觀測地點名稱 

print(f'{a}{b}，{weather[a][b]}。')

print(type(weather))
print(type(msg))
print(type(a))
print(type(b))
