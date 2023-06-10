from asyncio import threads
# import dis
import time

# def sum1(a, b):
#     return a + b


# dis.dis(sum1)


import threading

a = 0
threads_arr = []
lock = threading.Lock()

def x():
    global a
    lock.acquire()
    for _ in range(10_000):
        a += 1
    lock.release()


for _ in range(10):
    thread = threading.Thread(target=x)
    threads_arr.append(thread)
    thread.start()


for thread in threads_arr:
    thread.join()



print(a)
assert a == 100_000
