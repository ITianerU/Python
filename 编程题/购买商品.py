money = input()
list = input()
intList = []
for i in list.split(" "):
    intList.append(int(i))
sum = 0
buy_list = []
intList = sorted(intList)
print(intList)
for good in sorted(intList):
    sum = sum + good
    if sum <= int(money):
        buy_list.append(good)
    else:
        sum = sum - good
        break
print(sum)