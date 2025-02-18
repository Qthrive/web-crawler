import requests

cookies = {
    'SINAGLOBAL': '2825265488646.4136.1739863186538',
    '_s_tentry': '-',
    'Apache': '1215766542941.1235.1739874258941',
    'ULV': '1739874258949:2:2:2:1215766542941.1235.1739874258941:1739863186545',
    'SCF': 'AvaAArXGkU1NqZYBdAgSsmx2blTEBeNzlfO3cxWpKYaCj2i6CLu_EP8J0ImiRuBINDLvWbCAGNnLM218MOZVdbk.',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhBi0nVN3xWEWCl331Caw2n5JpX5KzhUgL.Foqpe0MXS0qp1hB2dJLoIEBLxKqL1heLBoeLxK-LBo5L12qLxKqLBKqL1K-LxKBLB.2L1hqt',
    'PC_TOKEN': 'afc29c0067',
    'UOR': ',,www.google.com',
    'ALF': '1742476136',
    'SUB': '_2A25KsPY4DeRhGeBP6FUV9yjNwziIHXVpzHfwrDV8PUJbkNANLULTkW1NRXdu02d3PmKdtZuz4zkokm2EfYvYYIKz',
    'SRT': 'D.QqHBJZPIVsBSimMb4cYGS4HAi!SPPZbuT!u35cbHNEYdVG9zSeWpMERt4EP1RckKA4uJP4o4TsVoObHRSG4nJcAq4FsISGMTWQfr5ck6T-rpMdSSWbbSN4kw*B.vAflW-P9Rc0lR-ykZDvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWfAc!nUbSKJ3YQMPWDUDJqJ4iYWqHli49ndDPI5cYPSrnlMcyoVF4nOPYOJGEnJdYCJcM1OFyHM4HJ5mkoODEfS4oCU-PJ5mjkOmH6i4noJeEJ5mkoOmHIV4noNpsJ5mkCOmzlJ!noTGEr',
    'SRF': '1739884136',
    'X-CSRF-TOKEN': 'CK-YcoCiN74-CoIiJ_5oxX9-gR0YC7I9NXSOEoEzCX5OCagix7u=',
}

headers = {
    'Host': 'passport.weibo.com',
    # 'Cookie': 'SINAGLOBAL=2825265488646.4136.1739863186538; _s_tentry=-; Apache=1215766542941.1235.1739874258941; ULV=1739874258949:2:2:2:1215766542941.1235.1739874258941:1739863186545; SCF=AvaAArXGkU1NqZYBdAgSsmx2blTEBeNzlfO3cxWpKYaCj2i6CLu_EP8J0ImiRuBINDLvWbCAGNnLM218MOZVdbk.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhBi0nVN3xWEWCl331Caw2n5JpX5KzhUgL.Foqpe0MXS0qp1hB2dJLoIEBLxKqL1heLBoeLxK-LBo5L12qLxKqLBKqL1K-LxKBLB.2L1hqt; PC_TOKEN=afc29c0067; UOR=,,www.google.com; ALF=1742476136; SUB=_2A25KsPY4DeRhGeBP6FUV9yjNwziIHXVpzHfwrDV8PUJbkNANLULTkW1NRXdu02d3PmKdtZuz4zkokm2EfYvYYIKz; SRT=D.QqHBJZPIVsBSimMb4cYGS4HAi!SPPZbuT!u35cbHNEYdVG9zSeWpMERt4EP1RckKA4uJP4o4TsVoObHRSG4nJcAq4FsISGMTWQfr5ck6T-rpMdSSWbbSN4kw*B.vAflW-P9Rc0lR-ykZDvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWfAc!nUbSKJ3YQMPWDUDJqJ4iYWqHli49ndDPI5cYPSrnlMcyoVF4nOPYOJGEnJdYCJcM1OFyHM4HJ5mkoODEfS4oCU-PJ5mjkOmH6i4noJeEJ5mkoOmHIV4noNpsJ5mkCOmzlJ!noTGEr; SRF=1739884136; X-CSRF-TOKEN=CK-YcoCiN74-CoIiJ_5oxX9-gR0YC7I9NXSOEoEzCX5OCagix7u=',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrf-token': 'CK-YcoCiN74-CoIiJ_5oxX9-gR0YC7I9NXSOEoEzCX5OCagix7u=',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://passport.weibo.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://passport.weibo.com/sso/signin?entry=wapsso&source=wapssowb&url=https%3A%2F%2Fm.weibo.cn%2F',
    'accept-language': 'zh-CN,zh;q=0.9',
    'dnt': '1',
    'sec-gpc': '1',
    'priority': 'u=1, i',
}

data = {
    'entry': 'wapsso',
    'source': 'wapssowb',
    'type': '1',
    'url': 'https://m.weibo.cn/',
    'username': '13291289190',
    'pass': '4147b4e939f6fcb63f3fd69000bb26ce5297cddd309d5fbd38e7a6667da87c65eb49d35ed144722b4b9c47bfe0d5db9837218db295c95d74bc3791d55f66a2a9b9d214460bef96e781da556cb8fd0c006e5ae5cef013c548d7a2d5c4beb664d21cf96b7863d0e92e84bc144694d6a2f3165bf3b3a9a8f5d6af50456b210b4b07',
    'pwencode': 'rsa',
    'rsakv': '1330428213',
}

response = requests.post('https://passport.weibo.com/sso/v2/login', cookies=cookies, headers=headers, data=data)
print(response.json())