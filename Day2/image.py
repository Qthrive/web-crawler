import requests
import os

image_url = "https://mfiles.alphacoders.com/828/828017.jpg"

response = requests.get(image_url,stream=True)

file_path = os.path.join('.','Day2','image.jpg')

if response.status_code == 200:
    with open(file_path,"wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print("保存成功")
else:
    print("失败")