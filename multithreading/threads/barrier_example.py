import time
import threading
import random


def barrier_func(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f'🔴 Поток {threading.current_thread().name} >> в {time.ctime()}')
    # Пока все потоки не дойдут до этой строчки, мы не продолжим выполнение кода
    # И все функции будут ждать.
    # Потом они одновременно смогут выполнить ниже идущий код
    barrier.wait()
    print(f'🟢 Поток {threading.current_thread().name} << в {time.ctime()}')


def barrier_example():
    bar = threading.Barrier(6)
    for i in range(6):
        threading.Thread(target=barrier_func, args=(bar,), name=f'thr-{i}').start()


if __name__ == '__main__':
    barrier_example()
