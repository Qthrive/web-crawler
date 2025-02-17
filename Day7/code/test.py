import requests
from lxml import etree

url = f'https://movie.douban.com/top250?start=0'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    "Cookie":'bid=JgE1tB35B_Q; ap_v=0,6.0; __utma=30149280.1943493433.1739439174.1739439174.1739439174.1; __utmc=30149280; __utmz=30149280.1739439174.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); push_noty_num=0; push_doumail_num=0; __utmt=1; __utmv=30149280.28696; dbcl2="286964664:xJc/sCfBNYk"; ck=bhE4; frodotk_db="843a16c65e232c8a8cae44531a69859e"; ll="108288"; __utmb=30149280.19.6.1739440854876; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1739440860%2C%22https%3A%2F%2Fwww.douban.com%2Flink2%2F%3Furl%3Dhttp%3A%2F%2Fwww.douban.com%2Fmovie%2Ftop250%22%5D; _pk_id.100001.4cf6=c3a5b68024ade6c4.1739440860.; _pk_ses.100001.4cf6=1; __utma=223695111.814996443.1739440860.1739440860.1739440860.1; __utmb=223695111.0.10.1739440860; __utmc=223695111; __utmz=223695111.1739440860.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/link2/'
}

response = requests.get(url,headers=headers).text
# print(response)

tree = etree.HTML(response)
item = tree.xpath('//div[@class = "item"]')
name = item[0].xpath('.//span[@class = "title"][1]/text()')
print(name)
director = item[0].xpath('.//p[1]/text()')[0].strip().split('导演: ')[1].split(' ')[0]
print(director)
pub_time = item[0].xpath('.//p[1]/text()')[1].strip().split('/')[0].strip()
# pub_time = item[0].xpath('.//p[1]/text()')[1]
print(pub_time)
# score = item[0].xpath('.//span[@class="rating_num"]/text()')[0]
score = item[0].xpath('.//span[@class="rating_num"]/text()')
print(score)
quote = item[0].xpath('.//span[@class="inq"]/text()')
print(quote)