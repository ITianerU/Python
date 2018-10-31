import re

#括号分组
s = r'([a-z]+) ([a-z]+)'
#re.I 忽略大小写
pattern = re.compile(s,re.I)
#match 从开始匹配,返回匹配的第一个
m = pattern.match("Hello World wide web")
#返回匹配的字符串
s = m.group(0)
print(s)
#返回匹配的字符串下标的跨度
a = m.span(0)
print(a)

#返回匹配的字符串的第一组
s = m.group(1)
print(s)
a = m.span(1)
print(a)

#返回匹配的每组字符串,turple
s = m.groups()
print(s)

