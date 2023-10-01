
class Foo:
    def __init__(self, data: int):
        self.data = data

    def __repr__(self) -> str:
        return f"Foo(data={self.data})"
    
a: Foo = Foo(1)
b: Foo = Foo(2)
a = None

c = b or a
print(c)
