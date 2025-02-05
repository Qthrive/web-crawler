import requests
from requests.exceptions import RequestException
import time
import os

token = os.getenv('GITHUB_TOKEN')

def download_image(url,filename):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Authorization":token
    }
    try:
        response = requests.get(url,headers=headers,stream=True,timeout=5)
        response.raise_for_status()
        filepath = os.path.join(".","Day2","github_image",filename)
        with open(filepath,"wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"下载成功:{filename}")
    except RequestException as e:
        print(f"下载失败，{e}")

def fetch_github_events(page = 1,per_page = 10):
    try:
        params = {
            'page':page,
            'per_page':per_page
        }
        response = requests.get("https://api.github.com/events",params=params,timeout=5)
        response.raise_for_status()
        events = response.json()

        for jdx,event in enumerate(events):
            avatar_url = event["actor"]["avatar_url"]
            username = event["actor"]["login"]
            extension = os.path.splitext(avatar_url)[1]
            filename = f"avatar_{username}.jpg"
            download_image(avatar_url,filename)
    except RequestException as e:
        print(f"请求失败:{e}")

if __name__ == "__main__":
    for page in range (1,2):
        fetch_github_events(page=page)
        time.sleep(1)