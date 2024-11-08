# Работа с переменными:
# 1 Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = 'No'

# 2 Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.
big_int = var_int * 3.5
print(big_int)
# 3 Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.
var_float = var_float - 1
print(var_float)

# 4 Разделите var_int на var_float, а затем big_int на var_float. Результат данных
# выражений не привязывайте ни к каким переменным.
print(var_int / var_float)
print(big_int / var_float)

# 5 Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации (+) и повторения строки (*).
var_str = var_str * 2 + 'Yes' * 3
print(var_str)

# 6 Выведите значения всех переменных.
print(var_int, var_float, var_str, big_int)

# Строки:
# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
i = 'Martsinkevich'
print(i[0])
print(i[-1])
print(i[2])
print(i[-3])
print(len(i))

# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
x = 'Martsinkevich Darya'
print(x[0:8])
print(x[8:12])
print(x[0:19:3])
print(x[::-1])

# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.
str_1 = 'my name is name'
print(str_1[:10] + str_1[10:].replace('name', 'Darya'))

# 4 Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
test_tring = "Hello world!"
print(test_tring.find('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))

# Списки:
# 1 Создайте два любых списка и свяжите их с переменными.
name = ['Darya', 'Anna', 'Ivan', 'Mihail']
surname = ['Martsinkevich', 'Volkova', 'Ivanov', 'Sokolov']

# 2 Извлеките из первого списка второй элемент.
print(name[1])

# 3 Измените во втором списке последний элемент. Выведите список на экран.
surname[-1] = 'Popov'
print(surname)

# 4 Соедините оба списка в один, присвоив результат новой переменной. Выведите
# получившийся список на экран.
full_name = name + surname
print(full_name)

# 5 "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
# обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
# значение этой переменной.
lst = full_name[3:5]
print(lst)

# 6 Добавьте в список два новых элемента и снова выведите его.
lst_name = full_name
lst_name.append('Sasha')
lst_name.append('Sidorov')
print(lst_name)

# 7 Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух
# списков. -- !не использовать циклы
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(set(a) & set(b))
print(result)

# 8 Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные
# значения. !не использовать циклы
c = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
num = list(set(c))
print(num)

# Логические операции:
# 1 Присвойте двум переменным любые числовые значения.
d = 15
e = 22

# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
exam = d > 6 and e > 9
exam_1 = d == 15 and e == 22
exam_2 = d < 6 and e < 7
exam_3 = d <= 20 and e < 22

# 3 Аналогично выполните п. 2, но уже используя оператор or.
exam_4 = d < 15 or d < 5
exam_5 = d > 8 or e < 25
exam_6 = d >= 15 or e > d
exam_7 = d == 22 or e == 15
print(exam_4, exam_5, exam_6, exam_7)

# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.
str1 = 'Hello'
str2 = 'Darya'
q = (len(str1) == 5) and (len(str2) == 5)
print(q)

# Словари:
# 1 Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
# 2б, 6а, 7в и т.д.).
school = {
    '1a': 28,
    '2a': 27,
    '3a': 26,
    '4a': 25,
    '5a': 24,
    '6a': 23,
    '7a': 22,
    '8a': 21,
    '9a': 20,
    '10a': 19
}

# 2 Узнайте сколько человек в каком-нибудь классе.
print(school['3a'])

# 3 Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
school['1a'] = 27
school['4a'] = 20
school['9a'] = 21
# ◦ в школе появилось два новых класса;
school['1b'] = 15
school['11a'] = 18
# ◦ в школе расформировали один из классов.
del school['6a']

# 4 Выведите содержимое словаря на экран.
print(school)

# Преобразование типов
# 1 Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
str3 = "Robin Singh"
str4 = "I love arrays they are my favorite"
print(list(str3.split()))
print(list(str4.split()))

# 2 Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
lst1 = ['Ivan', 'Ivanov']
str5 = 'Minsk'
str6 = 'Belarus'
print('Привет, ' + ' '.join(lst1) + '! Добро пожаловать в ' + str5, str6)

# 3 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
lst2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(lst2))

# 4 Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
lst3 = ['Dasha', 'Sasha', 'Masha', 'Glasha', 'Pasha', 'Stepan', 'Miron', 'Sifon', 'Anya', 'Manya']
lst3[2] = 'Dima'
del lst3[6]
print(lst3)

# 5 Есть 2 словаря
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
dct = {'a': 1, 'b': 2, 'c': 3}
dct1 = {'c': 3, 'd': 4, 'e': 5}
dct2 = {}

for key, value in dct.items():
    if key in dct1:
        dct2[key] = [dct[key], dct1[key]]
    else:
        dct2[key] = [value, None]
for key, value in dct1.items():
    if key in dct:
        dct2[key] = [dct[key], dct1[key]]
    else:
        dct2[key] = [None, value]
print(dct2)

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
arr = [1, 5, 2, 9, 2, 9, 1]
for i in arr:
    if arr.count(i) == 1:
        print(i)

# Условия
# 1 Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.
z = 10
if z > 0:
    z += 1
print(z)

# 2 Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.
v = 6
n = 14
m = -3
res = 0
if v > 0:
    res += 1
if n > 0:
    res += 1
if m > 0:
    res += 1
print('Колличество положительных чисел:', res)

# 3 Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).
year = 2024
if year % 4 == 0:
    print(366)
elif year % 100 == 0:
    print(365)
elif year % 400 != 0:
    print(365)
else:
    print(365)

# 4 Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).
day = 6
week = {
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "суббота",
    7: "воскресенье"
}
print(week[day])

# 5 Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.
number = 3
W = 1500
kg = {
    1: 1,
    2: 0.000001,
    3: 0.001,
    4: 1000,
    5: 100
}
result = W * kg[number]
print(result)

# Цикл for
# 1 Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.
A = 4
B = 9
C = 0
for o in range(A, B + 1):
    C += o
print(C)

# 2 Найти сумму всех натуральных чисел в от D до E
D = -3
E = 2
F = 0
for o in range(D, E):
    if o > 0:
        F += o
print(F)

# 3 Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
k = [1, 3, -5, -6, 2, 4, 7, -3, 9, 8]
pol = None
sum_neg = 0
col_neg = 0
for o in k:
    if o > 0:
        if pol is None:
            pol = o
        else:
            pol *= o
    elif o < 0:
        sum_neg += o
        col_neg += 1
print(pol, sum_neg, col_neg)

# 4 Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
resalt = {
    'Бекиш Александр': 21.07,
    'Будник Алексей': 20.34,
    'Гребень Анастасия': 22.12,
    'Давидович Татьяна': 30,
    'Дешук Дмитрий': 24.01,
    'Казак Анна': 28.17
}
mun = 60
for o in resalt:
    if resalt[o] < mun:
        mun = resalt[o]
print(mun)

# 5 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число
arr = [1, 5, 2, 9, 2, 9, 1]
for i in arr:
    if arr.count(i) == 1:
        print(i)

# Цикл while
# 1 Дано число N. Найти произведение всех чисел от 0 до N.
N = 5
ant = 0
while N > 1:
    ant *= N
    N -= 1
print(ant)

# 2 Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
S1 = 4
S2 = 6
years = 0
while S1 >= 0.1 * S2:
    S1 *= 2
    S2 *= 3
    years += 1
print(years)

# 3 Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.
N = 36
c = 0
while N > 0:
    c = c + N % 10
    N = N // 10
print(c)

# 4 Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.
M = 52
N = 4
year = 0
while N * 2 != M:
    M += 1
    N += 1
    year += 1
print(M, N, year)