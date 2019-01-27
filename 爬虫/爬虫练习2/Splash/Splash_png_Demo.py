
import requests


url = "http://localhost:8050/render.png?url=https://www.taobao.com&wait=5&width=1000&height=700"
rsp = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(rsp.content)
