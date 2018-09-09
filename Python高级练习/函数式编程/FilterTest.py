#过滤函数对列表,序列返回过滤后的可迭代的对象

def guoLu(n):
    return n > 5

fil = filter(guoLu,[1,4,7,5,4,7,8])
#和map一样只能使用一次
print([i for i in fil])

