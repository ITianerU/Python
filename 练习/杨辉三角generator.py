def gemerator1(n):
    l = [1]
    yield l
    for x in range(1,n):
        l = [1]+[l[i]+l[i+1] for i in range(x-1)]+[1]
        yield l

for i in gemerator1(20):
    print(i)
