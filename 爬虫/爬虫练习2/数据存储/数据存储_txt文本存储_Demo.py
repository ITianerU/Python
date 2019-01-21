
import requests
from pyquery import PyQuery

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}
html = requests.get(url=url, headers=headers).text
result = PyQuery(html)
items = result('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = result(item.find('.content').html()).text()
    with open('explore.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([question, author, answer]))
        f.write('\n' + '=' * 100 + '\n')
