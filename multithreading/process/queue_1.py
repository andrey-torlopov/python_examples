from ast import arg
from multiprocessing import Queue, Pipe, Process
from queue import Empty
from time import sleep


# def worker(a: int, q: Queue = None):
#     cnt = 0
#     while cnt < 3:
#         sleep(0.1)
#         q.put(11111)
#         cnt += 1
        
        
# def worker2(a: int, q: Queue):
#     cnt = 0
#     while nt < 3:
#         sleep(.1)
        

# ------------- пример 1


def worker(a: int, q: Queue) -> None:
    cnt = 0
    while cnt < 3:
        sleep(0.1)
        q.put(cnt)
        cnt += 1
    print("worker 1 ended")


def worker2(a: int, q: Queue) -> None:
    cnt = 0
    while cnt < 3:
        sleep(.1)
        cnt += 1
    
    try:
        print("!!!", q.get(timeout=1))
    except Empty as e:
        print("err", e)

    q.put(999)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(2, q))
    p1 = Process(target=worker2, args=(2, q))
    
    p1.start()
    p.start()
    
    # print(q.get())
    # print(q.get())
    # print(q.get())
    # print(q.get(timeout=1))
    
    try:
        for _ in range(10):
            print(q.get(timeout=1))
    except Empty as err:
        print("Empty q", err)

    p.join()
    p1.join()
    