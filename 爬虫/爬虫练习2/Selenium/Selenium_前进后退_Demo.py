
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

# 后退
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(1)
browser.get('https://www.taobao.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.close()
