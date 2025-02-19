import requests
import re
cookies = {
    'NMTID': '00OC6LxSgWqrBboYkZ4jTvdIJHkuLcAAAGVHfTv9Q',
    '_iuqxldmzr_': '32',
    'WEVNSM': '1.0.0',
    'WNMCID': 'hwamko.1739964348686.01.0',
    'WM_NI': 'yHntrUrdi1ur0%2Baf2sMzoWhW55Vd%2B0WaAJo7sp%2B6dpAXY76y1K2Ar58yEcwLKfKraZN5mg4JsJUle14i7QdNDF75%2FK0KchL3rlUD0rxpWyiK7cKe9FG7alkwjBmjZ%2BSSYm0%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eebbf773f2b1fe88b26283b88ba2c54f869f8aacc246a995fed7f944b3ec9d83c62af0fea7c3b92abb98a295f15fb2bca7d2f87af4f5af87b1798fa6a1b8eb5df7eb9a85aa3c95bf8fabee3db1b0e5d7e77c838897d8b573f395fea2f13ffca78b84f64889ba8593e4528eeba388b742b1969b8de83bf8b7f9b2e746889af9d6ae41f495ad89cf39b2b49ba5b37abcb0999aec41f5bd8586bc4e85e9af8dea7daa9ea38bd921918d978eb337e2a3',
    'WM_TID': 'dZR5PgdngiBBRQUVVELSJlKnrnDr9XPT',
    'ntes_utid': 'tid._.E8%252BTvT4gCVVEQkQUAALTIhfm%252B3CvswKE._.0',
    'sDeviceId': 'YD-g1VaRtMbB2JEE0FAFUKCM0e3qnTq8geS',
    '__snaker__id': '5Ni1jDRFxmp3oTrJ',
    'gdxidpyhxdE': 'ENmQC0RvYrH3Za83e%2FlpaEdyPq9QI17cagYPZBW2QNS%5CRe%5CrtPuzKr2CKpEgCZuxXWESUPymjfw%2B6qaSgVSLkyuqUek5ijirKQQcLqWig8rguGZhycP6szO67PaBwwe6YgHnObgGuu90eRJX5dQkW%2BftmKtp%2Fh1dXcsSpJM8rqut0%5C1r%3A1739965849645',
    'JSESSIONID-WYYY': 'Ypan02n8euGkg%2BzBC64yfMuKKJJxkgt9%2B%2BWt5Rxb%2FbfFvNbuhgQd0f9y4%5CKpe0g7P8F9BAq8mRXIalmCTPgQD0CG0E0dF8%2B%2BEYUGJ5rGl%2Bob1fT1ategQIpF%5CckXhKw95EG9F2%2BNH8fJUNKo82OSBDS%2BFV1A0apsA9n7G7PGaJE6Dxr5%3A1739968507134',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': 'NMTID=00OC6LxSgWqrBboYkZ4jTvdIJHkuLcAAAGVHfTv9Q; _iuqxldmzr_=32; WEVNSM=1.0.0; WNMCID=hwamko.1739964348686.01.0; WM_NI=yHntrUrdi1ur0%2Baf2sMzoWhW55Vd%2B0WaAJo7sp%2B6dpAXY76y1K2Ar58yEcwLKfKraZN5mg4JsJUle14i7QdNDF75%2FK0KchL3rlUD0rxpWyiK7cKe9FG7alkwjBmjZ%2BSSYm0%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebbf773f2b1fe88b26283b88ba2c54f869f8aacc246a995fed7f944b3ec9d83c62af0fea7c3b92abb98a295f15fb2bca7d2f87af4f5af87b1798fa6a1b8eb5df7eb9a85aa3c95bf8fabee3db1b0e5d7e77c838897d8b573f395fea2f13ffca78b84f64889ba8593e4528eeba388b742b1969b8de83bf8b7f9b2e746889af9d6ae41f495ad89cf39b2b49ba5b37abcb0999aec41f5bd8586bc4e85e9af8dea7daa9ea38bd921918d978eb337e2a3; WM_TID=dZR5PgdngiBBRQUVVELSJlKnrnDr9XPT; ntes_utid=tid._.E8%252BTvT4gCVVEQkQUAALTIhfm%252B3CvswKE._.0; sDeviceId=YD-g1VaRtMbB2JEE0FAFUKCM0e3qnTq8geS; __snaker__id=5Ni1jDRFxmp3oTrJ; gdxidpyhxdE=ENmQC0RvYrH3Za83e%2FlpaEdyPq9QI17cagYPZBW2QNS%5CRe%5CrtPuzKr2CKpEgCZuxXWESUPymjfw%2B6qaSgVSLkyuqUek5ijirKQQcLqWig8rguGZhycP6szO67PaBwwe6YgHnObgGuu90eRJX5dQkW%2BftmKtp%2Fh1dXcsSpJM8rqut0%5C1r%3A1739965849645; JSESSIONID-WYYY=Ypan02n8euGkg%2BzBC64yfMuKKJJxkgt9%2B%2BWt5Rxb%2FbfFvNbuhgQd0f9y4%5CKpe0g7P8F9BAq8mRXIalmCTPgQD0CG0E0dF8%2B%2BEYUGJ5rGl%2Bob1fT1ategQIpF%5CckXhKw95EG9F2%2BNH8fJUNKo82OSBDS%2BFV1A0apsA9n7G7PGaJE6Dxr5%3A1739968507134',
}

params = {
    'id': '3778678',
}
url = 'https://music.163.com/discover/toplist'
response = requests.get(url, params=params, cookies=cookies, headers=headers)
html = response.text
re_bds = r'<a href="/song\?id=(\d*?)">(.*?)</a>'
pattern = re.compile(re_bds)
res = pattern.findall(html)
# print(res)


def save_music():
    for i in range(5):
        id = res[i][0]
        name = res[i][1]
        url_music = rf'https://music.163.com/song/media/outer/url?id={id}'
        save_path = rf'D:\VScode\Crawler\Day11\output\{name}.mp3'
        content = requests.get(url_music,stream=True)
        with open(save_path,'wb') as f:
            for chunk in content.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f'{name}.mp3下载成功！')

save_music()