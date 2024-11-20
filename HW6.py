# 1 Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний
# и последний элементы данного файла. Если чисел меньше 3 выводить ошибку.
def first_task(file_name):
    with open(file_name, 'r') as file1:
        elements = file1.read().split()

        if len(elements) < 3:
            print('ERROR')

        else:
            print(elements[0], elements[1], elements[-2], elements[-1])


first_task('numb1.txt')


# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.
def second_task(numb):
    with open('numb1.txt', 'r') as file:
        numb = file.read().split()

    f1 = open('numb_even.txt', 'w')
    f2 = open('numb_odd.txt', 'w')

    for i in numb:
        if int(i) % 2 == 0:
            f1.write(i + '\n')
        else:
            f2.write(i + '\n')

    f1.close()
    f2.close()


second_task("numb1.txt")

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.


def third_task(file_name):
    with open(file_name, 'r') as file:
        elements = file.read().split()

    f = open('squares.txt', 'w')

    squared_numbs = [float(i) ** 2 for i in elements]

    for i in squared_numbs:
        f.write(str(i) + '\n')

    f.close()


third_task('numb1.txt')

# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
s = '10, 9, 8, 7, 6'
t = '5, 4, 3, 2, 1'

f = open('numb_bin1.bin', 'wb')
f.write(s.encode('utf-8'))
f.close()

f1 = open('numb_bin2.bin', 'wb')
f1.write(t.encode('utf-8'))
f1.close()


def fourth_task(numb_bin1, numb_bin2):
    with open(numb_bin1, 'rb') as file1:
        data1 = file1.read()
    with open(numb_bin2, 'rb') as file2:
        data2 = file2.read()

    with open('numb_bin1.bin', 'wb') as file1:
        file1.write(data2)
    with open('numb_bin2.bin', 'wb') as file2:
        file2.write(data1)


fourth_task('numb_bin1.bin', 'numb_bin2.bin')