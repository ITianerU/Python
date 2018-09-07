import zipfile
import os.path as op

#ZipFile 创建zip实例
zf = zipfile.ZipFile(op.join(op.abspath("."),"make_archive.zip"))

#getinfo 获取压缩包内文件信息
print(zf.getinfo("haha.txt"))

#namelist 获取文件列表
print(zf.namelist())

#extractall 解压
zf.extractall(op.join(op.abspath("."),"Zip_extract"))