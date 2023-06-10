import os
from time import sleep

# Создаем простой форк от процесса. И смотрим какой у него id

print(f"Начали работу в процессе {os.getpid()}")
res = os.fork()
print(f"Fork {os.getpid()} -> {res}")
print(f"Продолжаем работу в процессе {os.getpid()}")
sleep(100)
