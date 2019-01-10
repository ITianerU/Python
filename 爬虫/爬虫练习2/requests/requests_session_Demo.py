
import requests

# 多次访问维持同一会话
s = requests.session()
r = s.get('http://httpbin.org/cookies/set/number/123456789')
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)
