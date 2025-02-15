import re 

text = '<script>\
var data = { "name": "Alice", "age": 25 };\
console.log(data);\
</script>'

pattern = re.compile(r'<script>(.*?)</script>',re.DOTALL)

match = pattern.findall(text)
print(match)