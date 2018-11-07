from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
text = driver.find_element_by_id('wrapper').text
print(text)

driver.find_element_by_id("kw").send_keys("大熊猫")
driver.find_element_by_id('su').click()

time.sleep(2)
#快照
#driver.save_screenshot('panda.png')
print(driver.get_cookies())

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

driver.find_element_by_id('kw').send_keys('IU')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)

# 清空输入框 , clear
driver.find_element_by_id('kw').clear()
time.sleep(2)
driver.quit()