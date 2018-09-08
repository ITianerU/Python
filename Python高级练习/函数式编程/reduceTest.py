from functools import reduce

#归并操作,将第一项与第二项做操作后得出的结果,与第三项做操作,一次类推
def xiangChang(a,b):
    return a * b

print(reduce(xiangChang,[1,2,3,4,5]))