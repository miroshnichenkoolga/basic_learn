# Напишите функцию reverse_string(s), которая принимает строку и возвращает её в перевёрнутом виде.
# Подсказки:
# Можно использовать срезы [::-1].
# Можно использовать цикл или reversed().
# Пример использования:
# print(reverse_string("hello"))  # "olleh"
# print(reverse_string("Python")) # "nohtyP"

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # "olleh"
print(reverse_string("Python"))