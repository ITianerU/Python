import re

s = r"\d+"

pattern = re.compile(s)
#返回所有匹配的字符串,返回一个list类型
m = pattern.findall("qwe123rwes235434asdarqw654234asdf")
print(m)
#返回匹配所有字符串,返回一个迭代器
m = pattern.finditer("qwe123rwes235434asdarqw654234asdf")
for i in m:
    print(i.group())
