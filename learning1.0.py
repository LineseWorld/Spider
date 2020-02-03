import urllib.request
import ssl

# 请求打开baidu
# urlopen 默认是 Get 请求
response = urllib.request.urlopen('http://www.baidu.com')

# 输出html格式
# print(response.read().decode('utf-8'))

# 正则表达列子
import re
# 内容
content = 'Xiaoshuaib has 100 bananas'
# 规则
fil = '^Xi.*(\d+)\s.*s$'
res = re.match(fil,content)
print(res.group(1))