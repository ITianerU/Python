import os.path as op

#abspath 返回绝对路径
#.当前路径
print(op.abspath("."))
#..是父路径
print(op.abspath("..\\.."))

#basename 获取路径中文件名部分
print(op.basename("haha/haha1"))

#join 多个路径拼接
print(op.join("haha","haha1"))

#split 将路径与文件名分开
print(op.split("haha/haha1/haha2"))
print(op.split("haha\haha1\haha2"))

#isdir 检测是否是目录
print(op.isdir(op.abspath("..")))

#exists 检测文件或者路是否存在
print(op.exists(op.abspath("haha/haha")))