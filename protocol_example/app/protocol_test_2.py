from app.protocols.protocol_uno import UnoProtocol


def test_uno(u: UnoProtocol):
    u.uno()
    u.other_method()
