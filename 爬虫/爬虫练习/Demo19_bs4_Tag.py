from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)

html = rsp.read()

soup = BeautifulSoup(html, 'lxml')

print(soup.head)
print("*"*20)
print(soup.meta)
print("*"*20)
print(soup.link)
print("*"*20)
print(soup.link.attrs)