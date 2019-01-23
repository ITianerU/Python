
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

# 淘宝 操作输入框,点击按钮
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('switch')
time.sleep(2)
input.clear()
button = browser.find_element_by_css_selector('.btn-search.tb-bg')
button.click()


