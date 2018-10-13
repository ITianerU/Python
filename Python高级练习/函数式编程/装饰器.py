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



import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2018-10-13')

now()
print(now.__name__)

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        startTime = time.time()
        result = fn(*args,**kw)
        endTime = time.time()
        print('%s executed in %s ms' % (fn.__name__, endTime - startTime))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f == 33:
    print('测试成功!')
elif s == 7986:
    print('测试成功!')

#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#再思考一下能否写出一个@log的decorator，使它既支持：@log ;又支持：@log('execute')

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("begin call {}".format(text))
                result = func(*args, **kw)
                print('end call')
                return result
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print("begin call")
            result = text(*args, **kw)
            print('end call')
            return result
        return wrapper
@log
def a():
    print("hello")

@log("b")
def b():
    print("hello")

a()
b()

print("*"*50)
#一个函数同时装载多个装饰器,多个装饰器执行顺序
def dec1(func):
    print("1111")
    def one():
        print("2222")
        func()
        print("3333")
    return one

def dec2(func):
    print("aaaa")
    def two():
        print("bbbb")
        func()
        print("cccc")
    return two

@dec1
@dec2
def test():
    print("test test")

test()
#根据测试结果,可知先执行最下面的装饰器,函数被最下面的装饰器装饰后,装饰后的函数被倒数第二个装饰,以此往上执行,最后再执行原函数
/home/itianeru/PycharmProjects/Python/Python高级练习/函数式编程/装饰器.py