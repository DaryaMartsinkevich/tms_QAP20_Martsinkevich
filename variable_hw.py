def variables():
    # 1. Присваиваем значения переменным
    var_int = 10
    var_float = 8.4
    var_str = 'No'

    # 2. Увеличиваем значение var_int в 3.5 раза и сохраняем в big_int
    big_int = var_int * 3.5
    print("big_int:", big_int)

    # 3. Уменьшаем var_float на 1
    var_float -= 1
    print("var_float после уменьшения на 1:", var_float)

    # 4. Разделяем var_int на var_float, затем big_int на var_float
    print("var_int / var_float:", var_int / var_float)
    print("big_int / var_float:", big_int / var_float)

    # 5. Изменяем значение переменной var_str на "NoNoYesYesYes"
    var_str = var_str * 2 + 'Yes' * 3
    print("var_str:", var_str)

    # 6. Вывод всех переменных
    print("var_int:", var_int)
    print("var_float:", var_float)
    print("var_str:", var_str)
    print("big_int:", big_int)


# Вызов функции
variables()
