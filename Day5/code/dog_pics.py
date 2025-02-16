import requests
import os
import time
import random

current_dir = os.path.dirname(os.path.abspath(__file__))

# print(current_dir)

save_path = os.path.join(current_dir,'pics')

# print(save_path)

url = 'https://dog.ceo/api/breeds/image/random'

def save_image(url,path):
    try:
        response = requests.get(url,stream=True)
        response.raise_for_status()
        with open(path,'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f'save to {path} successfully!')
    except requests.RequestException as e:
        print(f'get error:{e}')
    except Exception as e:
        print(f'save error:{e}')

for i in range(1,21):
    response = requests.get(url)
    data = response.json()
    image_url = data['message']
    image_path = os.path.join(save_path,f'dog_{i}.jpg')
    save_image(image_url,image_path)
    time.sleep(random.uniform(1,2))

print('exit')