# Напишите функцию `generate_random_list(n, start, end)`, которая принимает три аргумента:
# - `n` – количество чисел в списке,
# - `start` – начало диапазона,
# - `end` – конец диапазона.
#
# Функция должна возвращать список из `n` случайных чисел в диапазоне `[start, end]`.
#
# ### Подсказки:
# - Используйте модуль `random` и функцию `random.randint()`.
import random

def generate_random_list(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

print(generate_random_list(5, 1, 10))