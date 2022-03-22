from threading import Thread
import random

import keyboard as keyboard

A = 200
q= 9
def prescript():
    global A
    global q
    while q!=0:
        while A < 100:
            b = random.randint(1, 100)
            A = A + b
            print('+', A)








def prescript2():
    global A
    global q
    while q != 0:
        while A >0:
            b = random.randint(1, 100)
            A = A - b
            print('-', A)
def stop():
    global A
    global q
    while q != 0:
        while A > 0:
            q = int(input())





thread1 = Thread(target=prescript)
thread2 = Thread(target=prescript2)
thread3 = Thread(target=stop)

thread1.start()
thread2.start()

thread3.start()
thread1.join()
thread2.join()

print('i',A)


