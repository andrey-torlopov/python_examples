import threading
import time


# Дата принимает данные только в своем потоке.
# Из другого потока мы не сможем значение проставить

data = threading.local()


def get():
    print(data.name)


def t1():
    data.name = f"T: {threading.current_thread().name}"
    time.sleep(1)
    get()


def t2():
    data.name = f"T: {threading.current_thread().name}"
    time.sleep(5)
    get()


def t3():
    try:
        get()
    except Exception:
        print("NO DATA in T3")


t1 = threading.Thread(target=t1, name="t1")
t2 = threading.Thread(target=t2, name="t2")
t3 = threading.Thread(target=t3, name="t3")

t1.start()
t2.start()
t3.start()
print(threading.enumerate())
t1.join()
t2.join()
t3.join()
