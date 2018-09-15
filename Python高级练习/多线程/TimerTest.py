import threading
import time

def a():
    print("aaaaaa")

if __name__ == '__main__':
    #十秒后执行a
    t = threading.Timer(10,a)
    t.start()