# 1 Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний
# и последний элементы данного файла. Если чисел меньше 3 выводить ошибку.
def first_task(numb):
    with open('numb1.txt', 'r') as file:
        numb = file.read().split()

    if len(numb) < 3:
        print('ERROR')

    else:
        print(numb[0], numb[1], numb[-2], numb[-1])


first_task('numb1.txt')

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.