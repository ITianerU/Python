
from urllib.request import build_opener, ProxyHandler
from urllib import error

# 代理
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9473',
    'https': 'https://127.0.0.1:9473'
})
opener = build_opener(proxy_handler)
try:
    response5 = opener.open('http://www.baidu.com')
    print(response5.read().decode('utf-8'))
except error.URLError as e:
    print(e.reason)
