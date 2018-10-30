import requests

url = "http://www.baidu.com"

#使用get请求
rsp = requests.get(url)
print(rsp.text)

#使用request请求
rsp = requests.request("get",url)
print(rsp.text)

kw = {
    "wd":"laowang"
}

url = "http://www.baidu.com/s?"
rsp = requests.get(url, params=kw)

print(rsp.text)