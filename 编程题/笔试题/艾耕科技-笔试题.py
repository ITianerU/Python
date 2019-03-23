"""
假设当前有100粒糖果分给10位小朋友,每一位小朋友得到的糖果数量随机,请问最终得到糖果数量第K多的小朋友得到了多少糖果,输入为一个长度为10的数组
每一为数字序号为下标的小朋友分到的糖果
输入:sugars=[10,30,5,7,12,20,3,3,10],k=3
输出:12
输入sugars=[20,20,15,15,5,5,2,3,2,3,10],k=2
输出:15
"""

sugars = input().replace("sugars=[", '').replace("]", '').replace("k=", "").split(",")
k = int(sugars.pop())
sugars = set(sugars)
sugars = list(map(lambda x: int(x), sugars))
sugars.sort(reverse=True)
print(sugars[k-1])

