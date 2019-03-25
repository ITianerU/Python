"""
题目:在某图形操作系统中,有 N 个窗口,每个窗口都是一个两边与坐标轴分别平行的矩形区域。窗口的边界上的点也属于该窗口。
    窗口之间有层次的区别,在多于一个窗口重叠的区域里,只会显示位于顶层的窗口里的内容。
    当你点击屏幕上一个点的时候,你就选择了处于被点击位置的最顶层窗口,并且这个窗口就会被移到所有窗口的最顶层,而剩余
    的窗口的层次顺序不变。如果你点击的位置不属于任何窗口,则系统会忽略你这次点击。
    现在我们希望你写一个程序模拟点击窗口的过程。
输入:输入的第一行有两个正整数,即 N 和 M。(1 ≤ N ≤ 10,1 ≤ M ≤ 10)
    接下来 N 行按照从最下层到最顶层的顺序给出 N 个窗口的位置。 每行包含四个非负整数 x1, y1, x2, y2,表示该窗
    口的一对顶点坐标分别为 (x1, y1) 和 (x2, y2)。保证 x1 < x2, y1 < y2。
    接下来 M 行每行包含两个非负整数 x, y,表示一次鼠标点击的坐标。
    题目中涉及到的所有点和矩形的顶点的 x, y 坐标分别不超过 2559 和 1439 。
输出:输出包括 M 行,每一行表示一次鼠标点击的结果。如果该次鼠标点击选择了一个窗口,则输出这个窗口的编号(窗口按照输
    入中的顺序从 1 编号到 N);如果没有,则输出”IGNORED”(不含双引号)。
输入样例:3 4
        0 0 4 4
        1 1 5 5
        2 2 6 6
        1 1
        0 0
        4 4
        0 5
输出样例:2
        1
        1
        IGNORED
"""
N_M = input().split(" ")
N = int(N_M[0])
M = int(N_M[1])
l = list()
for i in range(N):
    zb = list(map(lambda x: int(x), input().split(" ")))
    l.append(zb)
l2 = list(reversed(l.copy()))
for i in range(M):
    zb = list(map(lambda x: int(x), input().split(" ")))
    isFind = False
    for j in range(N):
        if zb[0] >= l2[j][0] and zb[0] <= l2[j][2] and zb[1] >= l2[j][1] and zb[1] <= l2[j][3]:
            print(l.index(l2[j])+1)
            l2.insert(0, l2.pop(j))
            isFind = True
            break
    if not isFind:
        print("IGNORED")