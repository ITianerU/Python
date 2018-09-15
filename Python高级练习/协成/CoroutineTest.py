#协成本质上是利用生成器
def coroutineA():
    print("laowang")
    i = yield
    print("laoli",i)
    i = yield
    print("laotian",i)
    i = yield

if __name__ == '__main__':
    a = coroutineA()
    a.send(None)
    a.send("你傻啊")
    a.send("hello")

#yield from
def a():
    for i in 'abc':
        yield i

def b():
    yield from 'def'

print(list(a()))
bb = b()
print(next(bb))
print(next(bb))
print(next(bb))
