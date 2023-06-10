from multiprocessing import Lock, Process, RLock
from random import random
from time import sleep



def file_writer(start: int, finish: int, lock: Lock) -> None:
    lock.acquire()
    for i in range(start, finish):
        with open("locker.txt", "a") as f:
            f.write(f"{i}\n")
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    p1 = Process(target=file_writer, args=(0, 5, lock))
    p2 = Process(target=file_writer, args=(5, 10, lock))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
