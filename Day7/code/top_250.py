import requests
import os
from lxml import etree
import csv
from datetime import datetime
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(current_dir,'douban_250.csv')

def fetch_250():
    headers = {
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    movies = []
    for i in range(0,250,25):
        url = f'https://movie.douban.com/top250?start={i}'
        try:

            response = requests.get(url,headers=headers)
            response.raise_for_status()
            html = response.text

            tree = etree.HTML(html)

            items = tree.xpath('//div[@class = "item"]')
            for item in items:
                name = item.xpath('.//span[@class = "title"][1]/text()')
                # print(name)
                director = item.xpath('.//p[1]/text()')[0].strip().split('导演: ')[1].split(' ')[0]
                # print(director)
                pub_time = item.xpath('.//p[1]/text()')[1].strip().split('/')[0].strip()
                # print(pub_time)
                score = item.xpath('.//span[@class="rating_num"]/text()')[0]
                # print(score)
                quote = item.xpath('.//span[@class="inq"]/text()')
                # print(quote)
                quote = quote[0] if quote else ''
                movies.append([name,director,score,pub_time,quote])
        except requests.RequestException as e:
            print(f'请求出错:{e}')
        except IndexError as e:
            print(f'解析出错:{e}')
        time.sleep(1)

    with open(save_path,'w',encoding='utf-8-sig',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["标题","导演","评分","出版时间","短句"])
        writer.writerows(movies)
    print('Save success!')

    report = f"# 豆瓣top250报告({datetime.now().strftime('%Y-%m-%d')})\n\n"
    report += "| 排名 | 标题 | 导演 | 评分 | 出版时间 | 短句 |\n|------|------|------|------|------|------|\n"
    for idx, movie in enumerate(movies, 1):
        report += f'| {idx} | {movie[0]} | {movie[1]} | {movie[2]} | {movie[3]} | {movie[4]} |\n'
    # 将报告保存到 Markdown 文件中
    with open(os.path.join(current_dir, 'report.md'), 'w', encoding='utf-8') as f:
        f.write(report)
    print('Save success!')

fetch_250()