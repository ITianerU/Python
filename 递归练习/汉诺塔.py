#汉诺塔
def func(n,a,b,c):
    if n==1:
        print(a,"-->",c)
        return None
    func(n-1,a,c,b)
    print(a,"-->",c)
    func(n-1,b,a,c)

a = 'A'
b = 'B'
c = 'C'
func(3,a,b,c)
