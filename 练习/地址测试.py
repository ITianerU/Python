def fun1(n):
    n[1]="2000"
    return None

def fun2(n):
    n+=100
    return None

a = [1,2,3,4]
b = 1.1
fun1(a)
fun2(b)
print(a)
print(b)

