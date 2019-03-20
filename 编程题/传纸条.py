first = list("ABCDEFGHI")
second = list("JKLMNOPQR")
third = list("STUVWXYZ*")
lists = [first, second, third]

date = input()
msg = input()
month = date.split(" ")[0]
day = date.split(" ")[1]
for i in range(int(month)-1):
    temp = lists[0]
    for j in range(1,3):
        lists[j-1] = lists[j]
    lists[2] = temp

for l in lists:
    for i in range(int(day)-1):
        temp = l[0]
        for j in range(1, 9):
            l[j - 1] = l[j]
        l[8] = temp

msg = list(msg)
zf = ''
for i in msg:
    for l in lists:
        if i in l:
            zf = zf+str(lists.index(l)+1)+str(l.index(i)+1)+" "
print(zf)




