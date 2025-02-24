import requests
from lxml import etree

def fetch_novel():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    url = 'https://www.doupocangqiong.org/doupocangqiong/18096.html'
    i = 1
    while True:
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        tree = etree.HTML(html)
        next_url = tree.xpath('//li [@class="col-md-4 col-xs-12 col-sm-12"]/a/@href')[0]
        if next_url == '/doupocangqiong/':
            break
        else:
            url = 'https://www.doupocangqiong.org/'+next_url
        title = tree.xpath('//h1/text()')[0]
        paras = tree.xpath('//comment()[.="adend"]/following-sibling::text()')
        content = '\n'.join(paras)
        with open(rf'C:\Users\93939\Desktop\douban\斗破苍穹\{i} {title}.txt','w',encoding='utf-8') as f:
            f.write(content)
        print(f'{title}保存成功！')

fetch_novel()

        
    

