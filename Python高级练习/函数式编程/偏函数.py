#用于类型转换 base表示当前输入的是什么进制,输出10进制
print(int("99999",base=16))

#偏函数,将函数的参数值固定,返回一个新函数
import functools
int8 = functools.partial(int,base=8)
print(int8("666"))