from lxml import etree
import matplotlib.pyplot as plt

# 解析 XML 文件
tree = etree.parse('books.xml')

# 定义 XPath 表达式，提取所有书籍的价格
path = '//book/price'
prices = tree.xpath(path)

# 提取价格数值
price_values = [float(price.text) for price in prices]

# 提取书籍标题，用于图表标签
titles = tree.xpath('//book/title')
title_values = [title.text for title in titles]

# 绘制柱状图
plt.bar(title_values, price_values)
plt.xlabel('Book Titles')
plt.ylabel('Prices')
plt.title('Book Prices')
plt.xticks(rotation=45)
plt.show()