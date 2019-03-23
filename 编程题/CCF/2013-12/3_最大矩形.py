"""
题目:在横轴上放了n个相邻的矩形，每个矩形的宽度是1，而第i（1 ≤ i ≤ n）个矩形的高度是hi。
    这n个矩形构成了一个直方图。例如，下图中六个矩形的高度就分别是3, 1, 6, 5, 2, 3。
    请找出能放在给定直方图里面积最大的矩形，它的边要与坐标轴平行。对于上面给出的例子，
    最大矩形如下图所示的阴影部分，面积是10。
输入:第一行包含一个整数n，即矩形的数量(1 ≤ n ≤ 1000)。
    第二行包含n 个整数h1, h2, … , hn，相邻的数之间由空格分隔。(1 ≤ hi ≤ 10000)。hi是第i个矩形的高度。
输出:输出一行，包含一个整数，即给定直方图内的最大矩形的面积。
输入样例:6
        3 1 6 5 2 3
输出样例:10
"""

n = int(input())
list_h = [int(i) for i in input().split(" ")]
max = 0
for i in range(n):
    count = 0
    # 查找当前矩形前边的矩形是否比当前矩形高或同高
    for j in range(i, -0, -1):
        if list_h[j] >= list_h[i]:
            count = count + 1
        else:
            break

    # 查找当前矩形后的矩形是否比当前矩形高或同高
    for j in range(i+1, n):
        if list_h[j] >= list_h[i]:
            count = count + 1
        else:
            break

    if count*list_h[i] > max:
        max = count*list_h[i]

print(max)
