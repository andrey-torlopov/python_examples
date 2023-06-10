import multiprocessing
import time


def end_func(response):
    print("end_func =", response)


def get_value(value):
    name = multiprocessing.current_process().name
    print(f'name: {name} value: {value}')
    time.sleep(1/3)
    return value


def out(x):
    print(f'value: {x}')
    return x


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        # p.map(get_value, list(range(100)))

        # Асинхронное выполнение с колбеком. Дожидаемся что вернеться.
        # И callback должен что-то вернуть. Переменная response для этого
        # p.map_async(get_value, list(range(100)), callback=end_func)
        
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func)

        p.close()
        p.join()
