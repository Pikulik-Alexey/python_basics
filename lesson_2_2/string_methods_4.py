# Перенос строки
print('Happy\nnew\nyear')

s = input('Введите ФИО: ')
print(s.replace(' ', '\n'))

# Разрезание строки
f, i, o = s.split()
print(f'Фамилия: {f}')
print(f'Имя: {i}')
print(f'Отчество: {o}')
str = f'| {f} | {i} | {o} |'
print('-' * len(str))
print(str)
print('-' * len(str))
