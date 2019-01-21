
from urllib.parse import urlencode
from pyquery import PyQuery
from pymongo import MongoClient
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    """
    获取页面
    :param page:
    :return:
    """
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        rsp = requests.get(url, headers=headers)
        if rsp.status_code == 200:
            return rsp.json()
    except requests.ConnectionError as e:
        print(e.args)


def parse_page(json):
    """
    解析数据
    :param json:
    """
    if json:
        items = json.get('data').get('cards')
        if len(items) > 0:
            item = items[0].get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = PyQuery(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comment_count')
            weibo['reposts'] = item.get('reposts_count')
            return weibo


def save_to_mongo(result):
    """
    保存到MongoDB
    :param result:
    """
    if collention.insert(result):
        print('successful')


if __name__ == '__main__':
    client = MongoClient()
    db = client['weibo']
    collention = db['weibo']
    for page in range(1, 11):
        json = get_page(page)
        result = parse_page(json)
        print(result)
        if result is not None:
            save_to_mongo(result)
