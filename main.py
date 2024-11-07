err = {
    'length': 'Длина пароля не равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
    'digits': 'Нет цифр в пароле',
    }

password = input('Пароль:')
if len(password) < 10:
    print(err['length'])
if password.islower() == True:
    print(err['upper'])
if password.isupper() == True:
    print(err['lower'])
if password.isdigit() == False:
    print(err['digits'])
else:
    print('PASS')