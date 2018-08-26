#斐波那契数列
def func(n):
	if n==1:
		return 1
	if n==2:
		return 1
	return func(n-1)+func(n-2)

for i in range(1,11):
    print(func(i),end=" ")
