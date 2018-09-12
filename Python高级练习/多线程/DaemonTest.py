#守护线程
import threading as t
import time
def fun():
    print("老王")
    time.sleep(2)
    print("你干啥呢")

t = t.Thread(target=fun)
#daemon 需要在start前面设置
#t.setDaemon(True)
t.daemon = True
t.start()
print("你是不似傻")