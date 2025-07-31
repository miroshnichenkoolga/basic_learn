import time
from functools import wraps

def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} executed in {elapsed} ms")
        return result
    return wrapper

@time_logger
def example_function():
    time.sleep(0.2)
    return "done"

print(example_function())