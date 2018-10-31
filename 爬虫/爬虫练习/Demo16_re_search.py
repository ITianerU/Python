import re

s = r"\d+"

pattern = re.compile(s)
m = pattern.search("qwe123rwes235434asdarqw654234asdf")
print(m.group())
#从指定位置查找,返回一个结果
m = pattern.search("qwe123rwes235434asdarqw654234asdf",10,20)
print(m.group())
