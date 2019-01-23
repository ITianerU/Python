
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script("alert('到底了')")
time.sleep(1)
# 获取alert弹窗
alert = browser.switch_to.alert
print(alert.text)
# 点击确定按钮
alert.accept()

