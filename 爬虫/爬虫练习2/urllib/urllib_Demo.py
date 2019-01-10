
from urllib import request, parse, error

response = request.urlopen("https://www.python.org")
print(response.read().decode('utf-8'))
print('=='*50)

# 状态码
print(response.status)
# 头信息
print(response.getheaders())
print(response.getheader('Server'))
print('=='*50)

# 转码
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
response2 = request.urlopen('http://httpbin.org/post', data=data)
print(response2.read().decode())
print('=='*50)

# 设置超时时间，过了时间服务器没有响应，会抛出URLError异常
try:
    response3 = request.urlopen('http://httpin.org/get', timeout=0.1)
    print(response3.read().deconde())
except error.URLError:
    print('Time Out')
print('=='*50)

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'httpbin.org'
}
data = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(data), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response4 = request.urlopen(req)
print(response4.read().decode('utf-8'))



