#! /usr/bin/python3
import sys
from datetime import datetime

# Принимаем параметры из командной строки


def main(args):
    ans = 1
    for arg in args[1:]:
        ans *= int(arg)
    print("calculated result as: {} on: {} ".format(ans, datetime.now()))


if __name__ == '__main__':
    main(sys.argv)
