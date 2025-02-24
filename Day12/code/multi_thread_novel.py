import asyncio
import aiohttp
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import requests

async def fetch_url(session, url, headers):
    async with session.get(url, headers=headers) as response:
        response.encoding = 'utf-8'
        html = await response.text()
        tree = etree.HTML(html)
        next_url = tree.xpath('//li [@class="col-md-4 col-xs-12 col-sm-12"]/a/@href')[0]
        return url, next_url

async def collect_chapter_urls(start_url, headers):
    urls = []
    url = start_url
    async with aiohttp.ClientSession() as session:
        while True:
            current_url, next_url = await fetch_url(session, url, headers)
            urls.append(current_url)
            print(f"网站{current_url}添加成功！")
            if next_url == '/doupocangqiong/':
                break
            url = 'https://www.doupocangqiong.org/' + next_url
    return urls

def fetch_and_save_chapter(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
        tree = etree.HTML(html)

        title = tree.xpath('//h1/text()')[0]
        paras = tree.xpath('//comment()[.="adend"]/following-sibling::text()')
        content = '\n'.join(paras)

        with open(rf'C:\Users\93939\Desktop\douban\斗破苍穹\{title}.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{title} 保存成功！')
    except Exception as e:
        print(f'抓取 {url} 时出错: {e}')

async def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    start_url = 'https://www.doupocangqiong.org/doupocangqiong/18096.html'

    # 异步收集所有章节 URL
    chapter_urls = await collect_chapter_urls(start_url, headers)

    # 使用线程池下载并保存章节内容
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_and_save_chapter, url, headers) for url in chapter_urls]
        for future in futures:
            future.result()

if __name__ == "__main__":
    asyncio.run(main())