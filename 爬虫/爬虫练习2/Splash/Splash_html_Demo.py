
import requests


url = "http://localhost:8050/render.html?url=https://www.baidu.com"
rsp = requests.get(url)
print(rsp.text)
