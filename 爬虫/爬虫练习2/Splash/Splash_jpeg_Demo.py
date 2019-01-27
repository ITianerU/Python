
import requests


url = "http://localhost:8050/render.jpeg?url=https://www.taobao.com&wait=5&width=1000&height=700"
rsp = requests.get(url)
with open('taobao.jpeg', 'wb') as f:
    f.write(rsp.content)
