from jsonpath_ng import parse

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

expr = parse('$..social.weibo')

matches = [match.value for match in expr.find(data)]
print(matches[0])