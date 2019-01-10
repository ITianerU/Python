
from urllib import error
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener

# 验证
username = 'username'
password = 'password'
url = 'http://www.baidu.com'
# 创建密码管理对象
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except error.URLError as e:
    print(e.reason)
print('=='*50)



