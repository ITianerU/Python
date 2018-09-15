import threading
import time

#可被同一线程多次访问,多用于递归
rlock = threading.RLock()

class RLockTest(threading.Thread):
    def run(self):
        global num,rlock
        for i in range(20):
            if(i < 10):
                rlock.acquire()
                print("第{}次申请锁".format(i+1))
            if(i >= 10):
                num = i-10
                rlock.release()
                print("第{}次释放锁".format(num+1))

if __name__ == '__main__':
    rl = RLockTest()
    rl.start()

