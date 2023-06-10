from multiprocessing import Pipe, Process
from queue import Empty
from time import sleep

# Если нужно из разных процессов события прокидывать, то
# надо дополнительно lock прокидывать и вручную лочить.


def pipe_worker(p: Pipe) -> None:
    some_data = 10_000
    p.send(some_data)


def pipe_worker_2(p: Pipe) -> None:
    p.send(111)
    print(p.recv())


if __name__ == '__main__':
    # Работа с конвеером
    parent_pipe, child_pipe = Pipe(duplex=False)
    p = Process(target=pipe_worker, args=(child_pipe, ))
    p1 = Process(target=pipe_worker_2, args=(child_pipe,))
    p.start()
    p1.start()

    print("Info from child process: ", parent_pipe.recv())
    parent_pipe.send("Info из главного процесса")

    p.join()
    p1.join()
