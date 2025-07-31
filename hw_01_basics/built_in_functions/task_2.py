# Напишите функцию filter_even(nums), которая принимает список чисел и возвращ.
# cписок только чётных, используя filter.
def filter_even(num):
    return list(filter(lambda x: x % 2==0, num))

print(filter_even([1, 2, 3, 4, 5, 6]))