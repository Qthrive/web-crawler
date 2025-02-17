import requests
import os
from lxml import etree
import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo

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

weather_data = {
    "date":date,
    "wea":wea,
    "high_temp":high_tem,
    "low_temp":low_tem,
    "wind":win
}

save_path = os.path.join(path,'weather.db')

def save_to_db(data,save_path,city = "武汉"):
    conn = sqlite3.connect(save_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT NOT NULL,
            date TEXT,
            weather TEXT,
            high_temp TEXT,
            low_temp TEXT,
            wind TEXT,
            update_time TIMESTAMP
        )
    ''')

    cursor.execute("DELETE FROM weather WHERE city =?", (city,))

    # 获取中国时区
    shanghai_tz = ZoneInfo('Asia/Shanghai')
    current_time = datetime.now(shanghai_tz).strftime('%Y-%m-%d %H:%M:%S')

    for i in range(len(data["date"])):
        cursor.execute('''
            insert into weather(city,date,weather,high_temp,low_temp,wind,update_time)
            values(?,?,?,?,?,?,?)
    ''',(city,data["date"][i],data["wea"][i],data["high_temp"][i],data["low_temp"][i],data["wind"][i],current_time))
    

    conn.commit()
    conn.close()

save_to_db(weather_data,save_path)
print('Save success!')