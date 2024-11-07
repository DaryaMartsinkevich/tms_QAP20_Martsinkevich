# 1. Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99
print(int(a))
print(int(b))

# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
line = 'www.my_site.com#about'
line_2 = line.replace('#', '/')
print(line_2)

# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
str = 'stroka'
str_2 = 'ing'
result = str + str_2
print(result)
# 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = 'Ivanou Ivan'
name_2 = name.replace('Ivanou Ivan', 'Ivan Ivanou')
print(name_2)
# 5. Напишите программу которая удаляет пробел в начале, в конце
# строки
word = ' Welcome '
word_delete = word.strip()
print(word_delete)
# 6. Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {
    '1a': 15,
    '2a': 16,
    '3a': 17,
    '4a': 18,
    '5a': 19,
    '6a': 20,
    '7a': 21,
    '8a': 22,
    '9a': 23,
    '10a': 24
}
print(school)
# 7. Создайте список и извлеките из него списка второй элемент.
list_family = ['Gena', 'Dasha', 'Dima', 'Ania']
print(list_family[1])
# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
stroka_1 = 'employ'
stroka_2 = 'employment'
print(stroka_1 in stroka_2)
# 9. Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])
# 10*. Есть массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
x = [1, 5, 2, 9, 2, 9, 1]
y = []

for i in x:
    if x.count(i) == 1:
        y.append(i)
print(y)