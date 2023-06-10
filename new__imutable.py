class CustomTuple(tuple):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, args)
        instance.property1 = kwargs.get('property1', None)
        instance.property2 = kwargs.get('property2', None)
        return instance


# Пример использования
t = CustomTuple(1, 2, 3, property1='value1', property2='value2')

print(t)  # (1, 2, 3)

print(t.property1)  # value1
print(t.property2)  # value2
