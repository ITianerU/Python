try:
    a = int(input("请输入一个数字"))
    print(1/a)
except ZeroDivisionError as e:
    print(e.args)
    print("不能输入0")
    #不执行try-finally之后的代码,退出程序
    #exit()
else:
    print("没有异常我执行")
finally:
    print("有没有异常我都执行")

#自定义异常
class lrtError(Exception):
    def __str__(self):
        return "自定义异常"

try:
    raise lrtError

except lrtError as e:
    print(e)

