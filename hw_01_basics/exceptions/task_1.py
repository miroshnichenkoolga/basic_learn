
def safe_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

print(safe_division(10, 2))   # 5.0
print(safe_division(5, 0))

