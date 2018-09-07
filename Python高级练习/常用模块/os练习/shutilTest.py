import shutil as s
import os.path as op
import os

#copy 拷贝文件 同时和重命名
#s.copy(op.join(op.abspath("."),"osTest.py"),op.join(op.abspath("."),"copyTest.py"))
#print(os.listdir())

#copy2与copy区别会尽量保留文件元数据

#copyfile 复制文件中的内容
# s.copyfile(op.join(op.abspath("."),"haha.txt"),op.join(op.abspath("."),"haha2.txt"))

#move 移动文件夹或文件
# s.move(op.join(op.abspath("."),"haha.txt"),op.join(op.abspath("."),"shutilTest"))

#make_archive 归档文件夹
# s.make_archive(op.join(op.abspath("."),"make_archive"),"zip",op.join(op.abspath("."),"shutilTest"))

#unpack_archive 解压
s.unpack_archive(op.join(op.abspath("."),"make_archive.zip"),op.join(op.abspath("."),"shutilTestUnpack_archive"))
