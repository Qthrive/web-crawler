from lxml import etree
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(current_dir,"tencent.html")

with open(html_path,'r',encoding='utf-8') as f:
    html = f.read()

tree = etree.HTML(html)

# news_title = tree.xpath('//div[@class = "question-title"]/text()')

# cleaned_title = [title.strip().replace('\n','').replace(' ','') for title in news_title]

# for title in cleaned_title:
#     print(title)

# news_link = tree.xpath('//a[@class = \'question-item\']/@href')

# for link in news_link:
#     print(link)

# images_link = tree.xpath('//img[@class = \'question-image\']/@src')

# for link in images_link:
#     print(link)

news_list = []

for i in range (1,31):
    title = tree.xpath(f'//a[@class = "question-item"][{i}]//div[@class = "question-title"]/text()')
    link = tree.xpath(f'//a[@class = "question-item"][{i}]/@href')
    image = tree.xpath(f'//a[@class = "question-item"][{i}]//img[@class = \'question-image\']/@src')

    news_list.append(
        {
            "title":title,
            "link":link,
            "image":image
        }
    )

save_name = "qq_news.json"

save_path = os.path.join(current_dir,save_name)

with open(save_path,"w",encoding='utf-8') as f:
    json.dump(news_list,f,ensure_ascii=False,indent=2)
print("Save succes!")