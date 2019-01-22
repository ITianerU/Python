
import requests
from urllib.parse import urlencode
import time
import os
from hashlib import md5
from multiprocessing import Pool

def get_page(offect):
    """
    获得json
    :param offect:
    :return:
    """
    params = {
        'offect': offect,
        'format': 'json',
        'keyword': 'IU',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return rsp.json()
    except requests.ConnectionError as e:
        return None

def get_images(json):
    """
    获取图片url列表
    :param json:
    :return:
    """
    image_list = []
    if json.get('data'):
        for item in json.get('data'):
            if item.get('image_list'):
                image_list.append(item.get('image_list'))
    return image_list

def save_image(url):
    """
    保存图片
    :param url:
    """
    file_name = url.split('/')[-1]
    rsp = requests.get("http://p3.pstatp.com/large/pgc-image/" + file_name)
    path = 'images/{0}.jpg'.format(md5(rsp.content).hexdigest())
    if not os.path.exists(path):
        with open(path, 'wb') as f:

            f.write(rsp.content)
    else:
        print('已存在该图片')
        print(path)

def main(offect):
    json = get_page(offect)
    if json:
        image_list = get_images(json)
        for images in image_list:
            for image in images:
                save_image(image.get('url'))

    time.sleep(1)


if __name__ == '__main__':
    pool = Pool()
    list = [i for i in range(0, 60, 20)]
    pool.map(main, list)
    pool.close()
    pool.join()
