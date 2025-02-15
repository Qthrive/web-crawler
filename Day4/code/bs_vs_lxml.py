import time
from bs4 import BeautifulSoup
from lxml import etree

# 准备测试用HTML（大文件更明显）
with open(r'D:\VScode\Crawler\Day4\code\tencent.html', "r",encoding='utf-8') as f:
    html = f.read()

# BeautifulSoup测试
start = time.time()
soup = BeautifulSoup(html, "html.parser")
soup.find_all("div", class_="question-title")
print(f"BeautifulSoup耗时：{time.time() - start:.4f}s")

# lxml测试
start = time.time()
tree = etree.HTML(html)
tree.xpath('//div[@class = "question-title"]/text()')
print(f"lxml耗时：{time.time() - start:.4f}s")