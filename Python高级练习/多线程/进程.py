import multiprocessing
import time

def a():
    while True:
        print("laowang~~")
        time.sleep(2)

class BProcessing(multiprocessing.Process):
    def run(self):
        while True:
            print("laoli~~")
            time.sleep(1)


if __name__ == '__main__':
    #直接生辰Process对象
    p = multiprocessing.Process(target=a)
    p.start()
    # 派生类创建进程
    bp = BProcessing()
    bp.start()
    p.join()
    bp.join()

