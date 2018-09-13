import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()
def fun1():
    #2秒没申请到锁,就释放自己的锁
    lock1.acquire(timeout=2)
    print("锁1")
    time.sleep(2)
    a = lock2.acquire(timeout=2)
    if a:
        print("锁2")
        lock2.release()
    lock1.release()

def fun2():
    lock2.acquire(timeout=2)
    print("锁2")
    time.sleep(4)
    a = lock1.acquire(timeout=2)
    if a:
        print("锁1")
        lock1.release()
    lock2.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()