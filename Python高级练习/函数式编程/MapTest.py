#将制定的列表,序列中的元素以一定的规则进行操作,,生成一个新的列表或集合

a = [1,2,3,4,5]

def num10(n):
    return n*10
b = list(map(num10,a))
print(type(b))


for i in b:
    print(i)

#map返回的迭代器,使用一次就会被清空,所以这里会输出[]
#可用list方法转化类型,就可以多次使用
c = [i for i in b]
print(c)


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    def fn(x):
        return x[0].upper()+x[1:].lower()
    return map(fn,name)
L1 = ['adam', 'LISA', 'barT']
print(list(normalize(L1)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    num1 = s.split(".")[0]
    num2 = sorted(s.split(".")[1],reverse=True)
    def fn1(x,y):
        return x*10+y
    def fn2(x,y):
        return x*0.1+y
    def fn3(x):
        return DIGITS[x]
    return reduce(fn1,map(fn3,num1))+reduce(fn2,map(fn3,num2))*0.1
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


