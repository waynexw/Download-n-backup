import urllib.request
url = 'http://news.baidu.com/sports'
#创建request对象
req = urllib.request.Request(url)
#发送请求，获取结果
with urllib.request.urlopen(req) as response:
data = response.read()
content = data.decode()
print(content)
