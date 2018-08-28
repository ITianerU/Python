#remove和discard的区别

a = {1,2,3,4}

a.discard(1000) #不报错

print("*"*20)
a.remove(10000) #报错
