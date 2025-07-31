from contextlib import contextmanager

@contextmanager
def ListContextManager(my_list):
    backup = my_list
    try:
        yield my_list
    finally:
        my_list.clear()
        my_list.extend(backup)

my_list = [1, 2, 3]
with ListContextManager(my_list) as lst:
    lst.append(4)
    print("Inside context:", lst)  # [1, 2, 3, 4]
print("Outside context:", my_list)  # [1, 2, 3]
print("-" * 30)

class ListContextManager:
    def __init__(self, lst):
        self._lst = lst
        self._backup = None

    def __enter__(self):
        self._backup = self._lst.copy()
        return self._lst

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lst.clear()
        self._lst.extend(self._backup)
        return False

my_list = [1, 2, 3]
with ListContextManager(my_list) as lst:
    lst.append(4)
    print("Inside context:", lst)   # [1, 2, 3, 4]

print("Outside context:", my_list)  # [1, 2, 3]