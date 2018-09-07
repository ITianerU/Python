import os

#getcwd 获取工作路径
print(os.getcwd())

#chdir 设置工作路径
os.chdir("\github")
print(os.getcwd())

#listdir 查看当前目录下文件/文件夹
print(os.listdir())

#makedirs 创建文件夹,可创建嵌套文件夹
# os.makedirs("osTest\osTest")

#mkdir 创建文件夹,不能嵌套
# os.mkdir("osTest2")

#system 执行系统命令
os.system("python -h")

#getenv 获取环境变量
print(os.getenv("classpath"))

#putenv 设置环境变量
# os.putenv("haha","haha")
# os.environ["haha"]="haha"
#print(os.getenv("haha"))

#curdir 当前目录
print(os.curdir)

#pardir 当前父目录
print(os.pardir)

#sep 当前系统路径分割付
print(os.sep)

#linesep 当前系统换行符
print("hello",os.linesep,"yah")

#name 当前系统名称
print(os.name)
"""
nt:是windows
posix:是Linux、Unix或Mac OS X
"""
