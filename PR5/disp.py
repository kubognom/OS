import threading
import time
import random

Pause = False
stop = False
break_ = False
pot_off = False
now = 0


class C1(threading.Thread):
    def __init__(self):
        super(C1, self).__init__()
        self.iterations = 0
        self.daemon = True  # Allow main to exit even if still running.
        self.paused = True  # Start out paused.
        self.state = threading.Condition()

    def run(self):
        global Pause
        global stop
        global break_
        global pot_off
        global now
        self.resume()

        print(now)
        AA = 1

        while True:
            with self.state:
                if self.paused:
                    self.state.wait()  # Block execution until notified.

            AA += random.randint(1, 30)
            print(AA)

            if AA >= 200:
                stop = True
                print('stop')
                pot_off = True
                break
            if AA <= 0 and now + 20 > time.time():
                print("q")
                pot_off = True

                break_ = True
            if now + 10 < time.time():
                print("pause")
                pot_off = True

                Pause = True

            time.sleep(1)
            self.iterations += 1

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.


class C2(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(C2, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        while True:
            print("C2")

    def off_C(self):
        self._event.set()


class C3(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(C3, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        while True:
            print("C2")

    def off_C(self):
        self._event.set()


class potok(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(potok, self).__init__(*args, **kwargs)
        self._event = threading.Event()

    def run(self):
        global break_
        global pot_off

        while True and pot_off == False:

            pott = str(input())
            if pott == 'q':
                break_ = True
                break

    def off_C(self):
        self._event.set()


def win_init():
    thread_list = []
    pausedthread = []
    pause_list = []
    global Pause
    global stop
    global break_
    global pot_off
    global now

    M = 1
    while M != 0:
        # event = str(input("input"))

        thread_viboor = int(input("ADD 1 module>> |ADD 2nd>> |ADD 3rd>> |Replace 4>>> |Wait->Start 6 >> | 5-start >> "))

        if thread_viboor == 1:
            thread_list.append(C1())
        if thread_viboor == 2:
            thread_list.append(C2())
        if thread_viboor == 3:
            thread_list.append(C3())
        if thread_viboor == 4:
            A = thread_list.pop(int(input("Kakoy potok B konez?>> ")) - 1)
            thread_list.append(A)
        if thread_viboor == 6:
            P = pause_list.pop(0)
            thread_list.append(P)
            pausedthread.append(P)
        if thread_viboor == 5:
            now = time.time()
            pot_off = False
            P = potok()
            P.start()

            B = thread_list.pop(0)
            for i in range(len(pausedthread)):
                if B == pausedthread[i]:
                    Pause = True
                else:
                    Pause = False
            print(B, " running")
            if Pause == False:
                B.start()
            B.resume()
            Pause = False

            while True:
                if break_ == True:
                    pause_list.append(B)
                    B.pause()
                    print("..")
                    P.join()
                    break_ = False
                    break

                if Pause == True:
                    B.pause()
                    thread_list.append(B)
                    pausedthread.append(B)
                    print("..")
                    P.join()
                    Pause = False

                    break
                if stop == True:
                    B.join()
                    print("..")
                    P.join()
                    stop = False
                    break

        pot_off == True
        print('potoki', thread_list)
        print('pause ', pause_list)


if __name__ == '__main__':
    win_init()
