
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# 获取属性
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo.get_attribute('class'))

input = browser.find_element_by_class_name('zu-top-add-question')
# 获取文本
print(input.text)
# 获取id
print(input.get_attribute('id'))
# 获取位置(坐标)
print(input.location)
# 获取标签名
print(input.tag_name)
# 获取大小(宽高)
print(input.size)

