# Пример с синглтоном

class Singletone:
    instanse = None

    def __new__(cls) -> 'Singletone':
        if cls.instanse is None:
            cls.instanse = super().__new__(cls)
        return cls.instanse


class Foo(Singletone):
    pass


a = Foo()
b = Foo()
print(a is b)
print(id(a), id(b))
