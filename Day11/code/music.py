import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'i',
    'range': 'bytes=0-',
    'referer': 'https://music.taihe.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'audio',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-storage-access': 'active',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

params = {
    'xcode': '21a0ee4cacc84509f4dfb2c1d7b126918d00288',
}

response = requests.get(
    'https://audio04.dmhmusic.com/71_53_T10064993476_128_4_1_0_sdk-cpm/cn/0209/M00/F5/46/ChR47GdJlZ2ASDUBAC3KnxBTiPA330.mp3',
    params=params,
    headers=headers,
    stream=True
)

with open(r'D:\VScode\Crawler\Day11\output\music.mp3','wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
print('success')