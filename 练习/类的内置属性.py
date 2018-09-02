class A():
    '''
    这是类文档
    '''
    name = "laowang"
    age = 16

#以字典的方式显示类的成员组成
print(A.__dict__)
#获取类的文档信息
print(A.__doc__)
#获取类的名称，如果在模块中使用，获取模块的名称
print(A.__name__)
#获取某个类的所有父类，以元组的方式显示
print(A.__bases__)