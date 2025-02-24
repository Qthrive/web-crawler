import requests
from lxml import etree
import re


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

url = 'https://www.doupocangqiong.org/doupocangqiong/18098.html'
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
html = response.text
# print(html)
tree = etree.HTML(html)
next_url = tree.xpath('//li [@class="col-md-4 col-xs-12 col-sm-12"]/a/@href')[0]
# re_bds_1 = r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br'
# re_bds_2 = r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<div class="m-page">'
# pattern_1 = re.compile(re_bds_1)
# pattern_2 = re.compile(re_bds_2,re.DOTALL)
# data_1 = pattern_1.findall(html)
# data_2 = pattern_2.findall(html)
# print(data_1)
# print(data_2)
# print(html)
# print(next_url) .replace('\xa0','')
passage = tree.xpath('//comment()[.="adend"]/following-sibling::text()')[0]
print(passage)
    

