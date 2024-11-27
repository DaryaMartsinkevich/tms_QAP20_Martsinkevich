import time

from HW.HW7 import numbers


# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы
def factorial(n):
    for i in range(4, n-1):
        if i > 0:
            return i


def factorial_generator(n):
    for i in range(n-1):
        if i > 0:
            yield i


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


factorial_time = time.time()
factorial(4)

generator_time = time.time()
factorial_generator(4)

recursive_time = time.time()
factorial_recursive(4)

print("Время работы факториала: ", factorial_time)
print("Время работы генератора: ", generator_time)
print("Время работы рекурсии: ", recursive_time)


# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args1 = []
            for i in args:
                if type == 'str':
                    args1.append(str(i))
                elif type == 'int':
                    args1.append(int(i))
                else:
                    args1.append(i)
            return func(*args1)
        return wrapper
    return decorator


@typed(type = 'str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(type = 'int')
def add_three_symbols(a, b, с):
    return a + b + с


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))


# 3 На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в
# английском языке.Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре
# встречается позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' <
# 'two'# является истинным)
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}


def sort_numbers_by_names(numb):
    return sorted(numb, key=lambda x: number_names[x])


numb = [8, 9, 16, 4, 0, 3, 11, 15]

sorted_numbers = sort_numbers_by_names(numb)
print(" ".join(map(str, sorted_numbers)))
