# Семафоры
#  Указываем количество потоков который хочет получить доступ к критической секции

import time
from threading import Thread, BoundedSemaphore, current_thread
import random

max_connection = 5

# по умолчанию value = 1
pool = BoundedSemaphore(value=max_connection)


def test():
    # Создает короткую запись, как с локом. Который внутрь помещает критическую секцию
    with pool:
        sleep_time = random.randint(3, 10)
        print(f"sleep for {sleep_time} sec:  ", current_thread().name)
        time.sleep(sleep_time)


for i in range(10):
    Thread(target=test, name=f'thr-{i}').start()
