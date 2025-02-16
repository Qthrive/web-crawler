def safe_get(data,*keys):
    current = data
    for idx,key in enumerate(keys):
        try:
            current = current[key]
        except(KeyError,TypeError,IndexError):
            raise ValueError(f'路径{keys[:idx+1]}不存在')
    return current

data = {
    "user": {
        "profile": {
            "social": {
                "weibo": "https://weibo.com/xxx",
                "twitter": None  # 可能缺失的字段
            }
        }
    }
}

try:
    weibo_url = safe_get(data,"user","profile","social","weibo")
    print(weibo_url)
except ValueError as e:
    print(e)
    weibo_url = "N/A"