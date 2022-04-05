import threading
import time
import random

q = 200


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        nums = range(1, 101)
        global q
        while q <= 100:
            if self._event.is_set():
                break
            num = random.choice(nums)
            q+=num
            print('произвед ', num)

            time.sleep(2 + random.random())
        while True:
            if q <= 80:
                if self._event.is_set():
                    break
                num = random.choice(nums)
                q+=num
                print('произвед ', num)
                time.sleep(2 + random.random())

    def off_P(self):
        self._event.set()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        global q
        nums = range(1, 101)
        while True:
            if self._event.is_set() and q<=0:
                print('ВСЁ')
                break
            if q>0:
                num = random.choice(nums)
                q -= num
                print('сьел', num)
                time.sleep(2.5 + random.random())

    def off_C(self):
        self._event.set()

def win_init():

    consumer_count = int(input("Сколько потребителей>>"))+1
    producer_count = int(input("Сколько производителей>> "))+1
    producer_list = []
    consumer_list = []
    while consumer_count > 1:
        consumer_list.append(Consumer())
        consumer_count-=1
    print(consumer_count)
    while producer_count > 1:
        producer_list.append(Producer())
        producer_count-=1

    global q

    while True:

        event = str(input("input"))

        if event == 'start' and producer_count != 0 and consumer_count != 0:
            for i in range(len(producer_list)):
                producer_list[i].start()
            for i in range(len(consumer_list)):
                consumer_list[i].start()
            producer_count = 0
            consumer_count = 0


        if event == 'q':
            print("Осталось:",q)
            for i in range(len(producer_list)):
                producer_list[i].off_P()
                producer_list[i].join()
            producer_list = []
            for i in range(len(consumer_list)):
                consumer_list[i].off_C()
                consumer_list[i].join()
            consumer_list = []
            event = ''
        if event == 'stop':
            break




if __name__ == '__main__':
    win_init()