import requests
import json
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer BQAvPTgZfJ_lnpga-8gICleRH4f5CbKnbkkKJugkkZIHGc08dCYU4AHe5RIIOVc4mkWTPWsznugwGqiCKN9SeANuYkZNs-SNJRX8g6IBa7YSC77ut5b2WGJWuDe8m-Sq9s4fs_3_SpLDCQjOEzQ6t5PafGbRktj473Iw34dJnwAKvBgGc7DjIE3bCaon4DXY1fQkObecfLKm0BkPESTENmRCFyZ-1mV4mVLxpt4QMARSOyQkUT1E5dbqVUARvBZkeKJXJHhXGS0uWqetvfiV-ozA861gyrbpDN0fOH3d0DBnPdKDWEJawK3O8trEskLdyBT2ESB4ZlV_sgY110GZWDTLIFcFitj0kAfXHhCRSPCwySsm30BESdiYhA',
    'cache-control': 'no-cache',
    'client-token': 'AABp7axgDXy44gUVs0f2VTbLQog9v999shMs7utESQuiJ5vQrKwTKF4XNFO3cuV0N04MXJ++7ndb3qgpGKKH0ZI5Vpf61ABY+fciAw23mQSYhaae3AtFEGsKCk/QytSu/04RQzqUXbCCvIhDDHiOTbfqWOWPtm93gqDE7grTElljZKTv42gy/g8aHWB4aAnjEgrraaQhELKyeeT+jkTUpYiOX13KWh0e6xnC8d562iFkfhgCOg+X2cR3XC0dryBYTPVqnLYAUIBzSVIuiqk/aCDLvxCLTQzm2FDYdfc5X8kIUF0=',
    'dnt': '1',
    'origin': 'https://open.spotify.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://open.spotify.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://api.spotify.com/v1/tracks?ids=2zjo2j5j3S0Nk21LKCgc8L,56mzU03ZesV0iRroHR2K04,0VqSdtXseb9khdZrnYVyM1&market=from_token',
    headers=headers,
)

print(response.json())

with open(r'D:\VScode\Crawler\Day11\output\Jay.json','w') as f:
    json.dump(response.json(),f,ensure_ascii=False,indent=2)

print('success')