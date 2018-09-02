class A():
    pass
def say(self):
    print("hello")
A.say = say
a = A()
a.say()

#方法绑定在对象上需要使用MethodType
from types import MethodType
def run(self):
    print("我能跑")
a.run = MethodType(run,A)
a.run()


#使用type创建类 arg1类名,arg2父类,arg3方法,属性
C = type("Chaha",(object,),{"run":run})
c = C()
c.run()
print(C.__dict__)

#使用元类创建类
class AMateClass(type):
    def __new__(cls, name, base, attrs):
        print("我是元类")
        attrs["name"] = "laoWang"
        return type.__new__(cls, name, base, attrs)
class A(object,metaclass=AMateClass):
    pass

a = A()
print(a.name)