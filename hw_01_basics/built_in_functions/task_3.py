# Напишите функцию `sort_words(words)`, которая принимает список строк и возвращает его, отсортированный в алфавитном порядке. Реализуйте **два варианта**:
#
# 1. С помощью встроенной функции `sorted`.
# 2. С помощью метода списка `.sort()` (не возвращает новый список, а меняет существующий).

def words_sorted(words):
    return sorted(words)

def words_sort(words):
    words.sort()
    return words


print(words_sorted(["banana", "apple", "cherry"]))  # ['apple', 'banana', 'cherry']

print((words_sort(["f", "a", "o"])))