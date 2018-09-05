import datetime as d

#datetime常见属性
#date:格式化为日期属性,年,月,日,时,分,秒
date = d.datetime(2018,9,5,9,34,5)
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)

#time:格式化为日期属性时,分,秒
time = d.time(2,3,4)
print(time)

#datetime模块:提供时间与日期的组合
from datetime import datetime
import time
"""
常用方法
today:返回当前时间
now:返回当前时间
fromtimestamp:从时间戳返回当前时间
"""
dt = datetime(1995,7,25)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

#timedelta模块,返回时间间隔
from datetime import timedelta

t1 = dt.now()
print(t1.strftime("%H:%M:%S"))
ttime = timedelta(hours=1)
print((t1+ttime).strftime("%H:%M:%S"))
