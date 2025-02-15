from lxml import etree

with open(r'D:\VScode\Crawler\Day4\code\tencent.html','r',encoding='utf-8') as f:
    html = f.read()

tree = etree.HTML(html)

news_title = tree.xpath('//div[@class = "question-title"]/text()')

cleaned_title = [title.strip().replace('\n','').replace(' ','') for title in news_title]

# for title in cleaned_title:
#     print(title)

# news_link = tree.xpath('//a[@class = \'question-item\']/@href')

# for link in news_link:
#     print(link)

images_link = tree.xpath('//img[@class = \'question-image\']/@src')
i=1
for link in images_link:
    print(f'{i}. '+link)
    i+=1