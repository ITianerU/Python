
import requests


url = "http://localhost:8050/render.har?url=https://www.jd.com&wait=5"
rsp = requests.get(url)
print(rsp.text)
