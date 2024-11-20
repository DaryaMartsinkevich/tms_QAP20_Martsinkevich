# 1. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
def unique_number(numb):
    unique = 0
    for i in numb:
        unique ^= i
    return unique


numbs = [1, 5, 2, 9, 2, 9, 1]
unique_number = unique_number(numbs)
print("Уникальное число:", unique_number)


# 2. Напишите программу которая удаляет пробел в начале, в конце строки
def spaces(text):
    return text.strip()


lst = " Hello "
new_lst = spaces(lst)
print(new_lst)
