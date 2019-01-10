
from requests import Request, Session

s = Session()
url = 'http://httpbin.org/post'
data = {
    'name': 'laoWang'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 '
                  'Safari/537.36 '
}
req = Request(url=url, method='POST', data=data, headers=headers)
# 转化为Prepare Request对象
prepend = s.prepare_request(req)
r = s.send(prepend)
print(r.text)
