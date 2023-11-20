from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
from json import loads
# Create your views here.
user_key = 'CWB-869C7631-CE97-4263-8AF8-635DF71E8A67'
doc_name = 'F-C0032-001'

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/%s?Authorization=%s" % (doc_name,user_key)


data = requests.get(url) #requests json檔內容為文字
#data = requests.get(url).text #type:str
print(type(data))

data_json = data.json() #轉換json格式 #type:dict
#data_json = json.loads(data)type:dict
print(type(data_json))

locations = data_json['records']['location'] #取出location內容，依照API資料結構從最外層的鍵開始取出


for i in locations: 
    city = i['locationName']    # 縣市名稱
    maxt8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
    ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
    pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    starttime = i['weatherElement'][1]['time'][0]['startTime'] #起始時間
    print(f'{city}未來 8 小時最高溫 {maxt8} 度，最低溫 {mint8} 度，天氣{wx8}，體感{ci8}，降雨機率 {pop8} %，從{starttime}開始 ')
print(type(i))
print(type(locations))
print(type(city))



