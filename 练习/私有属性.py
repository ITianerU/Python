class A():
    __name = "老李"

a = A()
#私有属性无法直接访问
#print(a.__name)  报错
#pytohn的私有是假私有，改了名字
#可以使用  _类名__属性名  访问私有属性

print(a._A__name)