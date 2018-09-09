#zip 将两个可迭代内容生成一个由tuple元素组成的可迭代内容,只能使用一次
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d',"e"]
z = zip(l1,l2)
for i,j in z:
    print(i,j)

#enumerate 将一个可迭代内容的每个元素配上索引组成tuple返回内容
enum = enumerate(l2)
print(list(enum))

#start 表示索引开始的值
enum2 = enumerate(l2,start=1000)
print(list(enum2))

#namedtuple 返回一个类
import collections

A = collections.namedtuple("A",['x','y'])
a = A(1,2)
print(a.x)
print(a[1])
print(type(a))
print(issubclass(A,tuple))

#deque
from collections import deque

b = deque([1,2,3,4])
b.append(5)
b.appendleft(0)
c = b.pop()
print(b)
print(c)

#defaultdict 当调用字典没有的kay时,返回默认值,参数为一个函数
from collections import defaultdict

f = lambda :"haha"

d = defaultdict(f)
d[1] = "a"
d[2] = "b"
print(d[1])
print(d[3])

#counter 统计字符串个数,返回键值对,键为字符,值为字符出现的个数
from collections import Counter

coun = Counter("qwkerjhqkjwerhasftyqwerjkasdfjkqwer")
print(coun)
