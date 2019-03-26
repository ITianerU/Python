"""
题目:给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。
输入:输入的第一行包含一个整数n，表示给定整数的个数。
    第二行包含所给定的n个整数。
输出:输出一个整数，表示值正好相差1的数对的个数。
输入样例:6
        10 2 6 3 7 8
输出样例:3
"""
n = int(input())
l = list(map(lambda x: int(x), input().split(" ")))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if abs(l[j]-l[i]) == 1:
            count = count + 1

print(count)
