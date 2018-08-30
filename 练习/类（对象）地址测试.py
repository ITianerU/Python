class A():
    name = "haha"
    age = 18
print(id(A.name))
print(id(A.age))
a = A()
#对象不对属性赋值，属性的地址还是类实例的属性地址
print(id(a.name))
print(id(a.age))
#对象对属性赋值，对象的属性地址改变
a.name = "heihei"
a.age = 99
print(id(a.name))
print(id(a.age))