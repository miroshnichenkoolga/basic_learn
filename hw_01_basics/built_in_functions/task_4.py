# Напишите функцию square_odds(nums), которая сначала отбирает только нечётные числа (с помощью filter),
# а затем возвращает список их квадратов (с помощью map).
def square_odds(num):
    return list(map(lambda x: x**2, filter(lambda x: x % 2!=0, num)))

print(square_odds([1, 2, 3, 4, 5]))