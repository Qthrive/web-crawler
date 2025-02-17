import requests
import os
from lxml import etree
import json
import sqlite3

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir,'weather')

url = 'https://www.weather.com.cn/weather/101200101.shtml'

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

tree = etree.HTML(html)

date = tree.xpath('//li[@class]/h1/text()')
# print(date)

wea = tree.xpath('//li[@class]/p[@title]/text()')
# print(wea)

high_tem = tree.xpath('//li[@class]/p[@class = "tem"]/span/text()')
# print(high_tem)

origin_low_tem = tree.xpath('//li[@class]/p[@class = "tem"]/i/text()')
low_tem = [tem.replace('℃','') for tem in origin_low_tem]
# print(low_tem)

win = tree.xpath('//li[@class]/p[@class = "win"]/i/text()')
# print(win)

sevendays_wea = []

for i in range(0,7):
    sevendays_wea.append({
        "date":date[i],
        "weather":wea[i],
        "high_temp":high_tem[i]+'℃',
        "low_temp":low_tem[i]+'℃',
        "wind":win[i]
    })

save_name = 'wuhan_7days_weather.json'

save_path = os.path.join(path,save_name)

with open(save_path,'w',encoding='utf-8') as f:
    json.dump(sevendays_wea,f,ensure_ascii=False,indent=2)
print("Save success!")

    