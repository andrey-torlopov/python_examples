def my_decorator(*dec_args, **dec_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            n = dec_kwargs.get("n", 0)
            print(f"n = {n}")
            print("Before call")
            result = 0
            for i in range(n):
                result += func(*args, **kwargs)
            print("After call")
            return result
        return wrapper
    return decorator


@my_decorator(n=10)
def add(x: int, y: int) -> int:
    return x + y


a = add(1, 2)
print(a)
