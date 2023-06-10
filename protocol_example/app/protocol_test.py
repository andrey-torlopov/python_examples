from .protocols.protocol_custom_uno import UnoProtocol


def test_uno(u: UnoProtocol):
    u.uno()
