from multiprocessing import Process  # Pool,
from random import random
from time import sleep


def file_writer(start: int, finish: int) -> None:
    '''На стороне ОС производится работа с семафором. Происходит блокировка. '''
    with open("locker.txt", "a") as f_o:
        for i in range(start, finish):
            sleep(random())
            print(i)
            f_o.write(f"{i}\n")


def file_writer2(start: int, finish: int) -> None:
    for i in range(start, finish):
        with open("locker.txt", "a") as f_o:
            sleep(random())
            print(i)
            f_o.write(f"{i}\n")


if __name__ == '__main__':
    p1 = Process(target=file_writer2, args=(0, 5))
    p2 = Process(target=file_writer2, args=(5, 10))
    print(p1.is_alive())
    print(p2.is_alive())
    p1.start()
    p2.start()
