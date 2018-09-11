#序列化,将变量存储在文件中
import pickle as p
a = "haha"
#b以二进制格式打开文件
with open("dalao.txt","wb") as f:
    p.dump(a,f)

#反序列化
with open("dalao.txt","rb") as f:
    b = p.load(f)
    print(b)
