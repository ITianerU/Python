from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)

html = rsp.read()

soup = BeautifulSoup(html, 'lxml')

tags = soup.find_all(name="meta")
print(tags)

#正则
import re
tags = soup.find_all(re.compile("^me"))
for i in tags:
    print(i)

print("*"*50)
tags = soup.find_all(re.compile("^me"), content="always")
print(tags)
