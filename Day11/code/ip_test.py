import requests
import json

with open(r'D:\VScode\Crawler\Day11\pre\ip_ports.json','r',encoding='utf-8') as file:
    data = file.read()

ip_ports = json.loads(data)
# print(ip_ports)



headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'dnt': '1',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1',
}

res = []

url = 'https://myip.ipip.net/'
for ip_port in ip_ports:
    proxy = {
        'http':f'http://{ip_port}',
        'https':f'https://{ip_port}'
    }
    try:
        response = requests.get(url,headers=headers,proxies=proxy,timeout=5)
        if response.status_code == 200:
            print(f'代理{ip_port}可用,响应内容:{response.text}')
            res.append(response.text)
        else:
            print(f"代理 {ip_port} 请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"代理 {ip_port} 发生错误：{e}")

with open(r'D:\VScode\Crawler\Day11\output\res.json','w',encoding='utf-8') as f:
    json.dump(res,f,ensure_ascii=False,indent=2)

print('Save success!')
