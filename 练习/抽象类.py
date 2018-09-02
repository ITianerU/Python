import  abc
class A(metaclass=abc.ABCMeta):
    #实例抽象方法
    @abc.abstractmethod
    def say(self):
        pass
    #类抽象方法
    @abc.abstractclassmethod
    def eat(cls):
        pass
    #静态抽象方法
    @abc.abstractstaticmethod
    def run():
        pass
class B(A):
    def say(self):
        print("我能说")
    def eat(self):
        print("我能吃")
    def run(self):
        print("我能跑")
b = B()
b.run()