a=[1,2,3,4,5]
b=[6,7,8,9,10]

print(id(a))
a.extend(b)
print(a)
print(id(a))


c=[1,2,3,4,5]
d=[6,7,8,9,10]

print(id(c))
c+=d
print(c)
print(id(c))

