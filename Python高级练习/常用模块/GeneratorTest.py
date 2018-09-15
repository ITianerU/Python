#使用()直接使用生成器
# (i for i in range(5))

def a():
    yield 1
    yield 2
    yield 3
    return "laoli"

g = a()
for a in g:
    print(a)

#斐波那契生成器
def b(max):
     count,a,b = 0,1,1
     while count<max:
         yield a
         a,b = b,a+b
         count += 1
     return "None"

for i in b(10):
    print(i)

#生成器的返回值,会出现在异常信息中
g2 = b(5)
for i in range(6):
    print(next(g2))