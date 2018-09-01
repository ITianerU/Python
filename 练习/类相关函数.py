class A():
    pass
class B(A):
    pass
class C(B):
    name = "LaoWang"

#arg1是否是arg2的子类
print(issubclass(B,A))

#arg1是否是arg2的对象
c = C()
print(isinstance(c,C))

#mro
print(C.__mro__)

#arg1是否有属性arg2
print(hasattr(C,"name"))

#获取指定属性的值
print(getattr(C,"name"))

#设置指定属性的值
setattr(C,"name","laoli")
print(getattr(C,"name"))

#获取属性列表
print(dir(C))

#删除指定属性
delattr(C,"name")
print(hasattr(C,"name"))

