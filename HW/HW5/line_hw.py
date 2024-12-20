# Строки:
# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
def first_task(text):
    if len(text) < 8:
        print("Строка содержит менее 8 символов")
        return

    first = text[0]
    last = text[-1]
    third_from_start = text[2]
    third_from_end = text[-3]

    length = len(text)
    print("Первый символ:", first)
    print("Последний символ:", last)
    print("Третий с начала:", third_from_start)
    print("Третий с конца:", third_from_end)
    print("Длина строки:", length)


first_task('Darya Martsinkevich')


# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку

def second_task():
    text = "Martsinkevich Darya"
    # Извлекаем первые восемь символов
    first_xt = text[:8]
    # Извлекаем четыре символа из центра строки
    center_x = text[9:13]
    # Извлекаем символы с индексами, кратными трем
    sign = text[::3]
    # Переворачиваем строку
    reversed = text[::-1]
    # Возвращаем все значения
    return first_xt, center_x, sign, reversed


# Вызов функции и вывод результатов
first_xt, center_x, sign, reversed = second_task()
print("Первые восемь символов:", first_xt)
print("Четыре символа из центра строки:", center_x)
print("Символы с индексами, кратными трем:", sign)
print("Перевернутая строка:", reversed)
