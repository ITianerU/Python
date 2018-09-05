#测量程序执行时间
import timeit

a = """
a = 1
b = 2
a,b = b,a
"""
b = """
a = 1
b = 2
temp = a
a = b
b = temp
"""
print(timeit.timeit(stmt=a,number=100000000))
print(timeit.timeit(stmt=b,number=100000000))

def hahaha():
    print("hahaha")
print(timeit.timeit(stmt=hahaha,number=100))

