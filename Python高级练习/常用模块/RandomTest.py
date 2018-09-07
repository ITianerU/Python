import random as r

#随机生成0-100的整数
print(int(r.random()*100))

#choice 随机返回序列中的某一个值
print(r.choice([1,2,3]))

#shuffle 打乱序列中的顺序
l = [1,2,3,4,5]
r.shuffle(l)
print(l)

#randint 随机产生整数
print(r.randint(0,100))