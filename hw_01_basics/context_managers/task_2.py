import time
from contextlib import contextmanager

@contextmanager
def time_tracker():
    start = time.time()
    try:
        yield
    finally:
        end= time.time()
        print(f"Время выполнения {end - start:.4f} секунд")

with time_tracker():
    # выполнение кода
    time.sleep(1)