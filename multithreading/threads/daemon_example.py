import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def example_1():
    thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1", daemon=True)
    thr.start()
    time.sleep(1)
    print("finish")


def get_data_2(data, value: int):
    for _ in range(value):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


def example_2():
    thread_list = []

    for i in range(3):
        thr = threading.Thread(target=get_data_2, args=(str(time.time()), i), name=f'thr-{i}')
        thread_list.append(thr)
        thr.start()

    for item in thread_list:
        item.join()

    print("finish")


# example_1()
# example_2()