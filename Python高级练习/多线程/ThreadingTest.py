import time
import threading
def print_1_10():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_a_z():
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i)
        time.sleep(1)
def main():
    t1 = threading.Thread(target=print_1_10)
    t1.start()
    t2 = threading.Thread(target=print_a_z)
    t2.start()
    t1.join()
    t2.join()
    print("---end---")

if __name__ == '__main__':
    main()