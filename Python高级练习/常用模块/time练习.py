import time as t
'''
time模块属性(utc世界时间)
timezone:当前时区和utc时间相差的秒数(无夏令时)
altzone:当前时区和utc时间相差的秒数(有夏令时)
daylight:当前是否是夏令时 0:不是
'''
print(t.timezone)
print(t.altzone)
print(t.daylight)

#时间戳
print(t.time())

#localtime,得到当前时间元组
print(t.localtime())

#ascctime,使用时间元组返回正常字符串时间格式 与localtime连用
print(t.asctime(t.localtime()))

#mktime,使用时间元组返回时间戳,与localtime连用,浮点型
print(t.mktime(t.localtime()))

#ctime,获取字符串化当前时间
print(t.ctime())

# sleep 是程序进入睡眠,定时执行
# 计时一分钟
for i in range(1,61):
    print(i)
    t.sleep(1)

#clock测试程序执行时间
a = t.clock()
t.sleep(5)
b = t.clock()
print(b-a)

#strftime 将时间元组格式化时间,与localtime连用
print(t.strftime("%Y-%m-%d %H:%M:%S",t.localtime()))
