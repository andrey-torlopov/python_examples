import os
from time import sleep

# print(f"Начинаем работу в процессе {os.getpid()}")
# res = os.fork()
# print(f"{os.getpid()} -> res")

# print(f"Начинаем работу в {os.getpid()}")

num_proc = int(input("Введите количество вызовов fork в цикле: "))

for i in range(num_proc):
    pid_marker = os.fork()
    if pid_marker != 0:
        print(f"Порождаю процесс {os.getpid()} -> {pid_marker}")

print(f">>>  Продолжаем работу в процессе {os.getpid()}")

sleep(100)
