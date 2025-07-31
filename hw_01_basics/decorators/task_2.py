# Создайте декоратор, который будет логировать вызовы функции:
# выводить имя функции и переданные ей аргументы.
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(arg) for arg in args]
        kwargs_list = [f"{k} ={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(args_list + kwargs_list)

        print(f"Calling {func.__name__} ({all_args})")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def example_function(a, b):
    return a + b

result = example_function(3, 7)
print("Result:", result)