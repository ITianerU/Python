import threading
import time
class A(threading.Thread):
    def __init__(self,arg):
        super(A,self).__init__()
        self.arg = arg
    #重写run
    def run(self):
        print(self.arg)
        time.sleep(1)

for i in range(10):
    a = A(i)
    a.start()
    a.join()
print("--end--")
