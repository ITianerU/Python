# a = open("laowang.txt","w")
# a.write("hahaha")
# a.close()

#with 语句自动关闭句柄
with open("laowang.txt","r",encoding="utf-8") as b:
    #读取一行
    l = b.readline()
    while l:
        print(l)
        l = b.readline()

#list 读取全部
with open("laowang.txt","r",encoding="utf-8") as b:
    l = list(b)
    for i in l:
        print(i)

#read 按照字符读
with open("laowang.txt","r",encoding="utf-8") as b:
    a = b.read(1)
    while a:
        print(a,end="")
        a = b.read(1)

#seek 移动文件读取的位置 0从头开始,1从当前位置开始,2从末尾开始
with open("laowang.txt","r",encoding="utf-8") as b:
    b.seek(4,0)
    l = b.read()
    print(l)

#tell 输出读取指针当前位置,以字节为单位
with open("laowang.txt","r",encoding="utf-8") as b:
    a = b.read(1)
    print(b.tell())
    while a:
        print(a,end=" ")
        a = b.read(1)
        print(b.tell())

#write,writelines 文件的写操作 , wirte只能字符串,wirteline可以字符序列
with open("laowang.txt","a",encoding="utf-8") as b:
    b.write("老王")
    b.write("你好")
    b.writelines(["haha","序列"])
