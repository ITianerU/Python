
import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)

