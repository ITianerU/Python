#集合交并差运算

a = {1,2,3,4,5}
b = {5,6,7,8,9}

#交集
c = a.intersection(b)
print(c)
#并集
c = a.union(b)
print(c)
#差集
c = a.difference(b)
print(c)
#是否为子集
a = {2,3,4}
b = {1,2,3,4,5}
c = a.issubset(b)
print(c)
#是否为超集
c = b.issuperset(a)
print(c)
