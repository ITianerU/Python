
import requests

# 传参
data = {
    'name': 'LaoWang'
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print(r.json())
