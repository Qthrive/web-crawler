from curl_cffi.requests import Session

session = Session(impersonate='chrome131')

url = 'https://tls.browserleaks.com/json'

response = session.get(url=url)

print(response.text)