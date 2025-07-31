# Задание 7. Подсчета суммы всех чётных чисел в списке
# Ожидаемый вывод ([1, 2, 3, 4, 5, 6]):
# 12

num = [4, 7, 1, 6, 8]

total = 0
for i in num:
    if i % 2 == 0:
        total += i
    else:
        continue
print(total)