"""
题目:给出一个字符串和多行文字，在这些文字中找到字符串出现的那些行。你的程序还需支持大小写敏感选项：
    当选项打开时，表示同一个字母的大写和小写看作不同的字符；当选项关闭时，表示同一个字母的大写和小
    写看作相同的字符。
输入:输入的第一行包含一个字符串S，由大小写英文字母组成。
　　 第二行包含一个数字，表示大小写敏感的选项，当数字为0时表示大小写不敏感，当数字为1时表示大小写敏感。
　　 第三行包含一个整数n，表示给出的文字的行数。
　　 接下来n行，每行包含一个字符串，字符串由大小写英文字母组成，不含空格和其他字符。
输出:输出多行，每行包含一个字符串，按出现的顺序依次给出那些包含了字符串S的行。
输入样例:
        Hello
        1
        5
        HelloWorld
        HiHiHelloHiHi
        GrepIsAGreatTool
        HELLO
        HELLOisNOTHello
输出样例:
        HelloWorld
        HiHiHelloHiHi
        HELLOisNOTHello
样例说明:在上面的样例中，第四个字符串虽然也是Hello，但是大小写不正确。
        如果将输入的第二行改为0，则第四个字符串应该输出
评测用例规模与约定: 1<=n<=100，每个字符串的长度不超过100。
"""
s = input()
isUpperOrLower = input()
n = int(input())

l = list()
l2 = list()
for i in range(n):
    l.append(input())

if isUpperOrLower == "0":
    l2 = list(map(lambda x: x.upper(), l))
    s = s.upper()
else:
    l2 = l.copy()

for i, item in enumerate(l2):
    if s in item:
        print(l[i])

