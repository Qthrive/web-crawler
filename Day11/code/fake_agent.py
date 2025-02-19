from fake_useragent import UserAgent
import requests

url = 'https://www.weather.com.cn/weather/101200101.shtml'

ua = UserAgent()

headers = {
    "User-Agent":ua.random,
    "Referer":'https://www.weather.com.cn/'
}

response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
html = response.text
print(html)