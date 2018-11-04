from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)

html = rsp.read()

soup = BeautifulSoup(html, 'lxml')

for i in soup.head.contents:
    if i.name == "meta":
        print(i)
    if i.name == "title":
        print(i.string)