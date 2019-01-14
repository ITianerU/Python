import requests
import re
import json
import time


def get_one_page(url):
    """
    :param url: 爬取的页面地址
    :return: 返回爬取的页面内容
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

    }
    rsp = requests.get(url, headers=headers)
    if rsp.status_code == 200:
        return rsp.text
    return None


def parse_one_page(html):
    """
    输出提取的数据
    :param html: 需要解析的html代码
    """
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?class="name">.*?>(.*?)</a>'
                         '.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(\d)</i>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5] + item[6]
        }


def write_to_file(content):
    """
    将数据写入json文件
    :param content: 爬去的数据
    """
    with open('maoyan.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    json_file = []
    for i in range(10):
        offset = str(i*10)
        url = 'https://maoyan.com/board/4?offset=' + offset
        html = get_one_page(url)
        for item in parse_one_page(html):
            json_file.append(item)
        time.sleep(1)

    write_to_file(json_file)

    with open('maoyan.json') as f:
        load_data = json.load(f)
        for item in load_data:
            print(item)
