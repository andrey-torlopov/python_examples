import time
import threading

# Lock - блокировка
# Разблокировать может любой кто имеет доступ к locker-у

locker = threading.Lock()


def inc_value():
    print(f"Блокируем поток... {threading.current_thread().name}")
    locker.acquire()
    print(f"Разблокируем поток... {threading.current_thread().name}")


t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)
t1.start()
t2.start()
print("Засыпаем на 2 секунды")
time.sleep(2)
locker.release()
print("Разблокировали")
print("finished")

# Пример с RLock
# Разблокировать может только поток который сделал блокировку.

# locker = threading.RLock()


# def inc_value():
#     print("Блокируем поток...")
#     locker.acquire()
#     print("Разблокируем поток...")


# t1 = threading.Thread(target=inc_value)
# t2 = threading.Thread(target=inc_value)

# t1.start()
# t2.start()
