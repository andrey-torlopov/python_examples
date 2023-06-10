# import random
import time
from multiprocessing import Condition, Event, Manager, Process

# Сложная тема. event.set() почему-то не отрабатывает. Надо после вызова 
# метод снова вызвать. И тогда он будет работать


def test(event: Event):
    print("test is running...")

    while True:
        print("...")
        if event.wait():
            print("test 1")
            event.clear()
        print("test 2")
        time.sleep(1)


def test_event(event: Event):
    while True:
        time.sleep(2)
        event.set()
        print("Event => True")
        time.sleep(2)
        event.clear()
        print("Event => False")


if __name__ == '__main__':
    with Manager() as manager:
        event = manager.Event()

        p = Process(target=test, args=(event,))
        p.start()

        p2 = Process(target=test_event, args=(event,))
        p2.start()

        p.join()
        p2.join()
