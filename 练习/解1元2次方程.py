from math import sqrt
def quadratic(a=0,b=0,c=0):
    if b*b-4*a*c<0:
        print("b^2-4ac<0,方程无实根")
        return None
    x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

x1,x2 = quadratic(2, 3, 1)

print("x1=",x1,"x2=",x2)
