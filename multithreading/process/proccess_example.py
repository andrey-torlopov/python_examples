import os
import time
from multiprocessing import Process

CNT = 0


def f():
    global CNT
    print("f started from: ", os.getpid())
    time.sleep(30)
    CNT += 2
    print(f"f: {CNT} from", os.getpid())


if __name__ == '__main__':
    p = Process(target=f, args=())
    print(p)
    # p_1 = Process(target=f, args=())
    # p_2 = Process(target=f, args=())

    p.start()
    # p_1.start()
    # p_2.start()
    print("finished")
