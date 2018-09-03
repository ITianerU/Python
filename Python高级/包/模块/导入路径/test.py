import sys

#添加搜索路径,不然找不到student
sys.path.append("D:\github\Python\Python高级\包\模块")

import student
a = student.student()
a.say()