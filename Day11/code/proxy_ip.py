from fake_useragent import UserAgent
import requests

url = 'https://www.weather.com.cn/weather/101200101.shtml'

ua = UserAgent()
proxies = {
    "http":'http://67.43.227.228:22103',
    "https":'https://67.43.227.228:22103'
}
headers = {
    "User-Agent":ua.random,
    "Referer":'https://www.weather.com.cn/'
}

response = requests.get(url,headers=headers,proxies=proxies)
response.encoding = 'utf-8'
html = response.text
print(html)