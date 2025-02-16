import requests
from datetime import datetime
import csv
import os

current_dir = os.path.dirname((os.path.abspath(__file__)))

url = 'https://api.bilibili.com/x/web-interface/popular'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=headers)

data = response.json()

videos = []

for video in data['data']['list']:
    pubdate = datetime.fromtimestamp(video['pubdate']).strftime("%Y-%m-%d %H:%M:%S")
    videos.append(
        {
            "aid":video['aid'],
            "bvid":video['bvid'],
            "标题":video['title'],
            "up主":video['owner']['name'],
            "播放量":video['stat']['view'],
            "点赞数":video['stat']['like'],
            "发布时间":pubdate,
            "封面":video['pic']
        }
    )

save_path = os.path.join(current_dir,'bilibili_hot.csv')

with open(save_path,'w',newline='',encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f,fieldnames=["aid","bvid","标题","up主","播放量","点赞数","发布时间","封面"])
    writer.writeheader()
    writer.writerows(videos)
    print('Save success!')