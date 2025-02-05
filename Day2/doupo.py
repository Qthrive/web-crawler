import requests

url = "https://www.doupocangqiong.org/doupocangqiong/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url=url,headers=headers)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("请求超时！")
except requests.exceptions.HTTPError as err:
    print(f"HTTP错误:{err}")
except requests.exceptions.RequestException as err:
    print(f"其他错误：{err}")

print(response.text)