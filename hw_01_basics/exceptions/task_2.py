def multiple_exceptions_handling(key1, key2):
    data = {"x": "10", "y": "0", "z": "abc"}
    result = None  # заранее объявляем переменную

    try:
        value1 = int(data[key1])
        value2 = int(data[key2])
        result = value1 / value2
    except KeyError as e:
        print(f"Ошибка: ключ {e} не найден в словаре")
    except ValueError as e:
        print(f"Ошибка: невозможно преобразовать значение в число — {e}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    else:
        print("Oшибок не возникло")
    finally:
        print("Завершение работы функции")

    return result

print(multiple_exceptions_handling("x", "y"))
print(multiple_exceptions_handling("a", "x"))

print(multiple_exceptions_handling("x", "x"))