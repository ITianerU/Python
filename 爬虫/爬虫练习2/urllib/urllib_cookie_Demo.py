
from http import cookiejar
from urllib import request

# cookie
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
rsp = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# cookie保存到文件中 Mozilla格式
filename = 'cookies.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# cookie保存到文件中 LWP格式
filename = 'cookies2.txt'
cookie = cookiejar.LWPCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取Mozilla格式cookie文件
filename = 'cookies.txt'
cookie = cookiejar.MozillaCookieJar()
cookie.load(filename, ignore_expires=True, ignore_discard=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
rsp = opener.open('http://www.baidu.com')
print(rsp.read().decode('utf-8'))
print('**'*50)

# 读取LWP格式cookie文件
filename = 'cookies2.txt'
cookie = cookiejar.LWPCookieJar()
cookie.load(filename, ignore_expires=True, ignore_discard=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
rsp = opener.open('http://www.baidu.com')
print(rsp.read().decode('utf-8'))
