# Напишите декоратор с параметром, который будет выполнять sleep на переданное количество секунд
# перед выполнением функции.
import time
from functools import wraps

def your_decorator(sleep_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {sleep_seconds} seconds before calling {func.__name__}")
            time.sleep(sleep_seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@your_decorator(sleep_seconds=3)
def some_func():
    print("Function is running!")

some_func()