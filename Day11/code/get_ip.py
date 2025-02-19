import requests
from lxml import etree
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

response = requests.get('https://free-proxy-list.net/', headers=headers)

html = response.text
tree = etree.HTML(html)
ip_ports = []
ips = tree.xpath('//table[@class = "table table-striped table-bordered"]/tbody/tr/td[1]/text()')
# print(ips)
ports = tree.xpath('//table[@class = "table table-striped table-bordered"]/tbody/tr/td[2]/text()')
# print(ports)
for i in range(len(ips)):
    ip_ports.append(
        ips[i]+':'+ports[i]
    )
# print(ip_ports)
with open(r'D:\VScode\Crawler\Day11\pre\ip_ports.json','w',encoding='utf-8') as f:
    json.dump(ip_ports,f,ensure_ascii=False,indent=2)
print('Save success!')