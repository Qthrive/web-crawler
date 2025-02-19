from curl_cffi import requests

url = 'https://ascii2d.net/'

response = requests.get(url,impersonate='chrome131')

print(response.text)