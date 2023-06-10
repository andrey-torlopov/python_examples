import time
import threading


def test():
    while True:
        print("test")
        time.sleep(1)


thr = threading.Timer(1, test)
# thr.daemon = True
thr.start()
