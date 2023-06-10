from ..protocols.protocol_custom_uno import UnoProtocol


class CustomUno(UnoProtocol):
    def uno(self):
        print("Other uno!")
