from app.protocol_test import test_uno
from app.protocol_test_2 import test_uno as test_uno_2

from app.models.uno import Uno
from app.models.custom_uno import CustomUno

if __name__ == '__main__':
    a = Uno()
    a1 = CustomUno()
    test_uno(a)
    test_uno(a1)

    test_uno_2(a)
