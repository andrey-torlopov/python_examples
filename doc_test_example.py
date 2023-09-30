
def foo(x):
    """
    Тестируем метод
    >>> a = 3
    >>> b = 5
    >>> a == b
    False
    >>> foo(3) == 3
    True
    """
    return x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
