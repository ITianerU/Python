#sorted

a = sorted([4,2,4,5,7,1])
print(a)

#从大到小排序
b = sorted([4,2,4,5,7,1],reverse=True)
print(b)

#按照绝对值排序
c = sorted([-4,2,4,5,-7,1],key=abs)
print(c)

#字母排序
d = sorted(['A','a','d','c'])
print(d)

#转换为小写字母排序,首位字母相同的情况下,比第二位
e = sorted(['Ab','a','d','c'],key=str.lower)
print(e)

