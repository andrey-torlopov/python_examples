import os
import multiprocessing
from multiprocessing import Pool
from time import sleep


def f(x: int) -> int:
    print(os.getpid(), "sleep!")
    sleep(1)
    return x * x


if __name__ == '__main__':
    pool = Pool(2)

    # Вызывает массив наших функций с параметрами. Выполнятся будут по 2 процесса.
    # res = pool.map(f, (1, 2, 3, 4, 5, 6))

    # Вызывает в нашем пуле разово метод.
    # 2 параметра не передашь, потому что ожидает 1 метод с 1 параметром
    # res = pool.apply(f, (2, 4))
    # print(res)
    
    # Тут формируем массив задач и когда вызываем .get() то происходит 
    # вызов процессов и получение результата
    # res = pool.map_async(f, (2, 3, 4, 5, 6, 7))
    # print(res)
    # print(res.get())

    multiple_result = [pool.apply_async(f, args=(i,)) for i in range(4)]
    # print(res.get())
    for res in multiple_result:
        print(res.get())
        
    # Нужно чтобы пул был по итогу закрыт и заджойнены процессы
    pool.close()
    pool.join()


# Для Pool можно использовать менеджер контекста

# with Pool(processes=4) as pool:
#     print(pool.map(f, range(10)))

