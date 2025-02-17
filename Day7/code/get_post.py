import requests

# GET请求（参数在URL）
get_response = requests.get("https://httpbin.org/get", params={"key1": "value1"})
print("GET URL:", get_response.url)  # 参数附加在URL

# POST请求（参数在请求体）
post_response = requests.post("https://httpbin.org/post", data={"key2": "value2"})
print(post_response.json())
print("POST Body:", post_response.json()["form"])  # 参数在form字段