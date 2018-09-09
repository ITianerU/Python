#函数可以当参数使用
def A():
    print("AAA")

def B(a):
    a()

B(A)

#函数当返回值使用
def C():
    def D():
        print("hello")
    return D

d = C()
d()

#函数闭包
def E(*args):
    def F():
        sum = 0
        for i in args:
            sum += i
        return sum
    return F
e = E(1,2,3,4,5,6,7,8,9)
print(e())

#闭包规定:返回闭包时,返回函数不能引用任何外部函数循环变量
def G():
    lf = []
    for i in range(1,4):
        def h():
            return i+i
        lf.append(h)
    return lf
#闭包在遇到外部函数循环时,直到循环结束才会执行return,所以闭包中的i都是3,返回值为6
g1,g2,g3 = G()
print(g1())
print(g2())
print(g3())

#解决上述问的方法,再嵌套一层函数
def G2():
    lf = []
    for i in range(1,4):
        def h(i):
            def h2():
                return i+i
            return h2
        lf.append(h(i))
    return lf
g1,g2,g3 = G2()
print(g1())
print(g2())
print(g3())