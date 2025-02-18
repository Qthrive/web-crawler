import requests
from urllib.parse import quote
import csv
from datetime import datetime
import os

hot_list = []

def fetch_hot():
    url = 'https://weibo.com/ajax/side/hotSearch'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    data = response.json()['data']
    # print(data)
    top = data['hotgovs'][0]
    top_title = top['name'].strip('#')
    try:
        label = top['icon_desc']
        # print(label)
        if label in ['新','爆','沸','热']:
            label = label
        else:
            label = ''
    except:
        label = ''
    top_link = f'https://s.weibo.com/weibo?q={quote(top_title)}&Refer=new_time'
    hot_list.append(
        [
            top_title,label,top_link
        ]
    )
    hots = data['realtime']
    for i in range(len(hots)):
        hot_title = hots[i]['word']
        try:
            label = hots[i]['icon_desc']
            if label in ['新','爆','沸','热']:
                label = label
            else:
                label = ''
        except:
            label = ''
        hot_list.append(
            [
                hot_title,label,f'https://s.weibo.com/weibo?q={quote(hot_title)}&Refer=new_time'
            ]
        )

def save_to_csv(hot_list):
    save_path = os.path.join(r'D:\VScode\Crawler\Day10\output',r'weibo_hot.csv')
    with open(save_path,'w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        time = datetime.now().strftime('%Y-%m-%d %H:%M')
        writer.writerow([time])
        writer.writerow(['标题','链接'])
        writer.writerows(hot_list)
    print('Save success!')


fetch_hot()
save_to_csv(hot_list)


