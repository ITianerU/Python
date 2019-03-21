"""
题目: 给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。
输入: 输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
     输入的第二行有n个整数s1, s2, …, sn (1 ≤ si ≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。
输出: 输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。
输入样例: 6
        10 1 10 20 30 20
输出样例: 10
"""

def show():
    num = input()
    l = input().split(" ")
    if int(num) != len(l):
        return
    d = dict()
    for i in l:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] = d[i] + 1
    max_value = max(d.values())
    temp = float("inf")
    for k, v in d.items():
        if v==max_value:
            k = int(k)
            if temp>k:
                temp = k;

    print(temp)

if __name__ == '__main__':
    show()