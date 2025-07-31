### Квадраты через `map`
# **Описание:**
# Напишите функцию `squares_map(nums)`, которая принимает список чисел и возвращает новый список их квадратов,
# используя `map`.
def squares_map(num):
    return list(map(lambda x: x **2, num))

print(squares_map([3, 2]))