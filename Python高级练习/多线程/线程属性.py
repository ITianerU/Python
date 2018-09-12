import threading as t
import time

def a():
    print("startA")
    time.sleep(3)
    print("endA")
def b():
    print("stratB")
    time.sleep(1)
    print("endB")

def main():
    t1 = t.Thread(target=a)
    t1.setName("laowang")
    t1.start()
    t2 = t.Thread(target=b)
    t2.setName("laojiang")
    t2.start()

    time.sleep(2)
    for i in t.enumerate():
        print(i.getName())
    print(t.activeCount())

if __name__ == '__main__':
    main()

