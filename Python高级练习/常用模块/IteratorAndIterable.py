from collections import Iterator,Iterable

#可迭代的
l1 = [1,2,3,4,5]
#迭代器
l2 = iter(l1)
print(isinstance(l1,Iterable))
print(isinstance(l2,Iterator))
for i in l2:
    print(i)

#迭代器的值只能用一次
for i in l2:
    #无输出
    print(i)