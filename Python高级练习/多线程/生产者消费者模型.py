import threading
import queue
import time

class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生成产品" + str(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    msg = self.getName() + '消费了' + q.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    q = queue.Queue()
    for i in range(500):
        q.put("初始产品"+str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()