import re 
import requests

url = "https://piaofang.maoyan.com/rankings/year"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple\
        WebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

html = requests.get(url=url,headers=headers).text

# .原来并不能匹配换行符，加入re.DOTALL参数从而可以匹配
pattern = re.compile(r'<p class="first-line">(?P<name>.*?)</p>',re.DOTALL)

names = pattern.findall(html)

for i in range(0,len(names)):
    print(f'{i+1}:'+names[i])