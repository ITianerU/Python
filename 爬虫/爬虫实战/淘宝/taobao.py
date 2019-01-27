
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
import time

# 启用无界面模式
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)
KEYWORD = 'switch'

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
MAX_PAGE = 10

def index_page(page):
    """
    抓取索引页
    :param page:
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = "https://s.taobao.com/search?q="+quote(KEYWORD)+"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190127&ie=utf8"

        browser.get(url)
        if page > 1:
            # 获取页码输入框
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            # 获取确定按钮
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        # 判断页面高亮的页码是否为,输入的页码
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        # 判断页面商品信息是否加载成功
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    获取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    """
    保存到MongoDB
    :param result:
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('save successful')
    except Exception:
        print('save faild')

def main():
    """
    遍历页码
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
        time.sleep(2)


if __name__ == '__main__':
    main()
