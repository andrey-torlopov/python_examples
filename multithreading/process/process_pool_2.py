import multiprocessing


def end_func(response):
    print("end_func", response)


def out(x, y, z):
    '''функция принимает 3 параметра'''
    print(f'value: {x} {y} {z}')
    return x + 1, y + 1, z + 1


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap(out, [(1, 2, 3), (4, 5, 6)])
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        p.close()
        p.join()
