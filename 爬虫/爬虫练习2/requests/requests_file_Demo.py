
import requests

# 上传文件
files = {
    'file': open('favicon.ico', 'rb')
}
data = {
    'name': 'laoWang'
}
r = requests.post('http://httpbin.org/post', files=files, data=data)
print(r.text)
print(r.json())
