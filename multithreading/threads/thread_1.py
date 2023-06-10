import glob
import time
import threading
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


def func_sleep():
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")
    time.sleep(1)
    print(f"Finished! {threading.get_ident()}")


def func_heavy_math():
    cnt = 0
    for _ in range(50_000_000):
        cnt += 1
    print(f"func_heavy_math >>  поток {threading.get_ident()} из процесса {os.getpid()}")

# ---


def test_1():
    # Линейно выполняем задачи 1 за другой
    start_time = datetime.now()
    func_sleep()
    func_sleep()
    func_sleep()

    total_time = datetime.now() - start_time
    print(f"Total time: {total_time}")


def test_2():
    start_time = datetime.now()
    th1 = threading.Thread(target=func_sleep)
    th2 = threading.Thread(target=func_sleep)
    th3 = threading.Thread(target=func_sleep)
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

    total_time = datetime.now() - start_time
    print(f"Total time: {total_time}")


def test_3():
    start_time = datetime.now()
    th1 = threading.Thread(target=func_heavy_math)
    th2 = threading.Thread(target=func_heavy_math)
    th3 = threading.Thread(target=func_heavy_math)
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()
    total_time = datetime.now() - start_time
    print(f"Total time: {total_time}")


def test_4():
    start_time = datetime.now()

    with ThreadPoolExecutor(max_workers=3) as t:
        [t.submit(func_heavy_math) for _i in range(3)]

    total_time = datetime.now() - start_time
    print(f"Total time: {total_time}")


# Global variable

CNT = 0


def func_cnt_printer_and_increment():
    global CNT
    CNT += 1
    print(f"func_cnt_printer_and_increment >>  поток {threading.get_ident()} из процесса {os.getpid()} cnt: {CNT}")


def test_5():
    # Треды шерят ресурсы, поэтому CNT увеличивается.
    # В процессах мы бы получили 1. Т.к. ресурсы разные.
    start_time = datetime.now()

    with ThreadPoolExecutor(max_workers=3) as t:
        [t.submit(func_cnt_printer_and_increment) for _i in range(3)]

    total_time = datetime.now() - start_time
    print(CNT)
    print(f"Total time: {total_time}")


test_5()
