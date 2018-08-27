#浅拷贝
a = [1,2,3,[4,5,6]]
b = a.copy()
print(id(a))
print(id(b))
b[3][2] = 600
print(a)
print(b)

#深拷贝
import copy
c = copy.deepcopy(a)
print(id(a))
print(id(c))
c[3][1] = 500
print(a)
print(c)
