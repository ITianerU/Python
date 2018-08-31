#实例化时先从本身上找构造,找不到就会找父类,再找父类的父类直到找到
class A():
    def __init__(self):
        print("hello")

class B(A):
    pass

class C(B):
    pass

C()