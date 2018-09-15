import threading
import time
#限制同时执行的线程数量
sem = threading.Semaphore(3)

def a():
    sem.acquire()
    for i in range(10):
        print(threading.currentThread().getName())
    time.sleep(20)
    sem.release()

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=a)
        t.start()
