password = input('Введите пароль: ')

while len(password) < 8:
    print(
        f'Длина пароля должна быть не менее 8 символов, а вы ввели длину {len(password)}')
    password = input('Введите пароль снова: ')
print(f'Поздравляем вы ввели пароль {password}')
