import threading
import time

sum = 0
#创建一个锁的对象,一把锁只能同时被一个线程访问
lock = threading.Lock()
def add():
    global sum
    for i in range(1,20):
        #申请锁
        lock.acquire()
        sum += 1
        print("add:",sum)
        #释放锁
        lock.release()
        time.sleep(1)

def subtract():
    global sum
    for i in range(1,20):
        lock.acquire()
        sum -= 1
        print("subtract:",sum)
        lock.release()
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=subtract)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end",sum)