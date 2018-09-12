import _thread as t
import time

def print_1_10():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_a_z():
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i)
        time.sleep(1)

#start_new_thread 第一个参数是方法名,第二个方法的参数,turple类型
def main():
    t.start_new_thread(print_a_z,())
    t.start_new_thread(print_1_10,())


#实际有三个线程,主线程不等待其他线程,直接回结束
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)