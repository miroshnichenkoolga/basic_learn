# Создайте декоратор, который будет кэшировать результат функции для заданных аргументов и возвращать
# сохранённый
# результат при повторных вызовах с теми же аргументами.
from functools import wraps

def cache_results(func):
    cache={}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print(f"Returning cached result for{func.__name__} {args} {kwargs}")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        print(f"Caching result for {func.__name__}{args} {kwargs}")
        return  result
    return wrapper

@cache_results

def expensive_computation(x, y):
    print(f"Computing {x} * {y}")
    return x * y

print(expensive_computation(2, 3))
print(expensive_computation(3, 2))

