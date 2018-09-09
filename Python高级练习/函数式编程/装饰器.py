#装饰器
def sayEveryOne(f):
    def everyOne(*args,**kwargs):
        print("everyone")
        return f(*args,**kwargs)
    return everyOne

@sayEveryOne
def a():
    print("hello")
a()

#手动使用装饰器

def b():
    pass
c = sayEveryOne(b)
c()

#函数被装饰了两次
print("*"*30)
d = sayEveryOne(c)
d()