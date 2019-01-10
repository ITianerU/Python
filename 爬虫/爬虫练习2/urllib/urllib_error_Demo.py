
from urllib import error, request
import socket

try:
    rsp = request.urlopen('https://bilibili.com/qwerqwer.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Successfully')
print('**'*50)

try:
    rsp = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    # 超时异常，e.reason返回的是对象
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('time out')
