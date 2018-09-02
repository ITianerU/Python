class A():
    name = "laoWang"
    age = 23
    def __init__(self,height):
        self._height = height
        print("创建对象时调用")
    def __call__(self):
        print("当对象被当做方法用时调用")
    def __str__(self):
        return "当对象被当做字符串用时调用"
    def __repr__(self):
        return "当对象被当做字符串用时调用"

    def __setattr__(self, key, value):
        super().__setattr__(key,value)
        print("设置属性时被调用")
    def __getattr__(self, item):
        print("获取不存在的属性值时被调用")
    def __delattr__(self, item):
        print("属性被删除时调用")

    #类比大小时调用
    def __gt__(self, other):
        return self._height > other._height
    #类相加时调用
    def __add__(self, other):
        return self._height + other._height


a = A(23)
a()
print(a)
a.name = "laoli"
print(a.haha)
delattr(a,"age")

c = A(99)
print(a<c)

print(a+c)