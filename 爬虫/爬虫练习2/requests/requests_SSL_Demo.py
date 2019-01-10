
import urllib3
import requests
import logging


# 设置忽略SSL验证的同时，忽略警告信息
# urllib3.disable_warnings()
# 捕获警告到日志的方式忽略警告
logging.captureWarnings(True)
# 忽略SSL验证
r = requests.get('https://www.12306.cn', verify=False)
print(r.status_code)
