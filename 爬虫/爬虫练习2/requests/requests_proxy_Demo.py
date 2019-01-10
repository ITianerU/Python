
import requests

proxies = {
    "http": 'http://10.10.1.10:3128',
    "https": "http://10.10.1.10.1080"
}

r = requests.get('https://www.taobao.com', proxies=proxies)
print(r.text)
