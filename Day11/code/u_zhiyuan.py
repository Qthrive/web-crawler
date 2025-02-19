from curl_cffi import requests

url = 'https://www.youzy.cn/tzy/search/colleges/collegeList'

cookies = {
    'connect.sid': 's%3AWC7e8B_b8iDEcCcdMRGBU3VW-hv8lwm0.trXJaHeXE%2BqeomsXrVE%2BkunrZWI7dDh%2F9hH7VQSwc3Y',
    'Youzy2CUFS': '2019YAfanti',
    'Youzy2CCurrentProvince': '%7B%22provinceId%22%3A%22849%22%2C%22provinceName%22%3A%22%E6%B9%96%E5%8C%97%22%2C%22isGaokaoVersion%22%3Afalse%7D',
    'youzy_full_ad': 'false',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.youzy.cn/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'dnt': '1',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1',
    # 'Cookie': 'connect.sid=s%3AWC7e8B_b8iDEcCcdMRGBU3VW-hv8lwm0.trXJaHeXE%2BqeomsXrVE%2BkunrZWI7dDh%2F9hH7VQSwc3Y; Youzy2CUFS=2019YAfanti; Youzy2CCurrentProvince=%7B%22provinceId%22%3A%22849%22%2C%22provinceName%22%3A%22%E6%B9%96%E5%8C%97%22%2C%22isGaokaoVersion%22%3Afalse%7D; youzy_full_ad=true',
}

response = requests.get('https://www.youzy.cn/tzy/search/colleges/collegeList', cookies=cookies, headers=headers,impersonate='chrome131')

with open(r'D:\VScode\Crawler\Day11\output\uzhiy.html','w',encoding='utf-8') as f:
    f.write(response.text)
print('success')