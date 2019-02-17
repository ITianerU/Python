
# 最大公约数
def gcd(a, b):
    if a % b == 0:
        return b
    t = a
    a = b
    b = t % b
    return gcd(a, b)

if __name__ == '__main__':
    print(gcd(1680, 640))
