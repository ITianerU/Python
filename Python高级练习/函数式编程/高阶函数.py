#函数可以当参数使用
def A():
    print("AAA")

def B(a):
    a()

B(A)