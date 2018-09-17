import re

a = re.compile(r"\d+")
#math 在起始位置进行匹配,匹配不到返回None
b = a.match("asdf123asdf123",4)
print(b)
print(b.group(0))
print(re.match("a","abcd").span())

#search 返回第一个匹配的结果
c = a.search("qwe123qweasdqwe123qwe")
print(c.group())

#findall 返回所有匹配结果list 若有多分组,会返回多个分组的匹配以tuple为单位的list
d = a.findall("qwe123qweasdqwe123qwe")
for i in d:
    print(i)
print("*"*20)
#finditer 返回所有的匹配的结果,可迭代
e = a.finditer("qwe123qweasdqwe123qwe")
print(type(e))
for i in d:
    print(i)

#sub 替换匹配的字符,返回修改后的字符串
f = a.sub("~~~","qwe123qweasdqwe123qwe")
print(type(f))

#匹配中文
chinese = re.compile(r"[\u4e00-\u9fa5]+")
g = chinese.findall("老王 老李 haha")
print(g)

#贪婪与非贪婪
h = re.compile(r"(\d+).*(\d+)") #贪婪
h2 = re.compile(r"(\d+).*?(\d+)") #非贪婪
print(h.search("123qwe123qwe123").group())
print(h2.search("123qwe123qwe123").group())