# Задание 8. Генерации ряда Фибоначчи до nго члена (где n вводится пользователем)
# Ожидаемый вывод (n=6):
# [0, 1, 1, 2, 3, 5]

num = int(input("Введите число: "))

fib =[]
if num >= 1:
    fib.append(0)
if num>=2:
    fib.append(1)

for i in range(2, num):
    next_num = fib[i -1] + fib[i - 2]
    fib.append(next_num)

print(fib)