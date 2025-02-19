### TLS,Akamai指纹绕过
#### 使用第三方库`curl_cffi`  
**示例代码**
```python
from curl_cffi.requests import Session

session = Session(impersonate='chrome131')

url = 'https://tls.browserleaks.com/json' # 测试网站

response = session.get(url=url)

print(response.text)
```

### 5秒盾同理
**示例代码**
```python
from curl_cffi import requests

url = 'https://ascii2d.net/' # 测试网站

response = requests.get(url,impersonate='chrome131')

print(response.text)
```