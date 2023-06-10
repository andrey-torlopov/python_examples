import time
import threading


def test():
    while True:
        print("test")
        time.sleep(1)


thr = threading.Timer(1, test)
thr.daemon = True
thr.start()


for i in range(3):
    print(f"second: {i}")
    time.sleep(1)

thr.cancel()
print("finish")
