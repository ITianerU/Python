
import re
import requests

# 传参
data = {
    'name': 'LaoWang'
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(r.json())

# 抓取知乎网页
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 '
                  'Safari/537.36 '
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取GitHub站点图标
r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as file:
    file.write(r.content)
