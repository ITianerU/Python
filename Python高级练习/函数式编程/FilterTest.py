#过滤函数对列表,序列返回过滤后的可迭代的对象

def guoLu(n):
    return n > 5

fil = filter(guoLu,[1,4,7,5,4,7,8])
#和map一样只能使用一次
print([i for i in fil])

#素数的生成器-----埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def primes():
    yield 2
    it = _odd_iter()
    def _not_divisible(n):
        return lambda x:x%n > 0
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for i in primes():
    if i<1000:
        print(i)
    else:
        break


#筛选回数
def is_palindrome(n):
    def fn(n):
        n = str(n)
        length = len(n)
        if length > 0:
            if length%2==0:
                if n[0:length//2]==n[length//2:]:
                    return True
                else:
                    return False
            else:
                if n[0:length//2]==n[length//2+1:]:
                    return True
                else:
                    return False
        else:
            return True
    return filter(fn,n)


print(list(is_palindrome(range(1000))))
