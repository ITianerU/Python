import requests

url = "https://fanyi.baidu.com/sug"
data = {
    "kw": "boy"
}
rsp = requests.post(url,data=data)

print(rsp.json())