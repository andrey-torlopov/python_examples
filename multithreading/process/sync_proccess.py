import os
import time
from datetime import datetime
from multiprocessing import Process


def sleeper(slp: int) -> None:
    time.sleep(slp)
    print(f"Process {os.getpid()} has been finished.")


if __name__ == '__main__':
    start = datetime.now()
    p = Process(target=sleeper, args=(10,))
    p1 = Process(target=sleeper, args=(100,))

    p.start()
    p1.start()

    p.join()
    print(f"Program in main proccess {os.getpid()} has been finishe: Total executen time: {datetime.now() - start}")
