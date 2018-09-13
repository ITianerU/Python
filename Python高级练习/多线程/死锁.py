import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()
def fun1():
    lock1.acquire()
    print("锁1")
    time.sleep(2)
    lock2.acquire()
    print("锁2")
    lock1.release()
    lock2.release()

def fun2():
    lock2.acquire()
    print("锁2")
    time.sleep(4)
    lock1.acquire()
    print("锁1")
    lock2.release()
    lock1.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()