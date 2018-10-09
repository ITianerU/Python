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


#测试