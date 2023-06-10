from time import sleep
from multiprocessing import Pipe, Process


def proc1(pipe):
    for i in range(1, 10):
        pipe.send(i)
        print(f"send {i} to pipe")
        sleep(1)


def proc2(pipe):
    n = 9
    while n > 0:
        result = pipe.recv()
        print(f"recieve {result} from pipe")
        n -= 1


def main():
    pipe = Pipe(duplex=False)
    print(type(pipe))

    p1 = Process(target=proc1, args=(pipe[1],))
    p2 = Process(target=proc2, args=(pipe[0],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    pipe[0].close()
    pipe[1].close()


if __name__ == '__main__':
    main()
