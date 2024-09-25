# Калькулятор с функциями

def get_number(promt):
    while True:
        value = input(promt)
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print('Это не целое число!')

# lambda функция

# add = lambda a, b: a + b
# subtract = lambda a, b: a - b
# multiplication = lambda a, b: a * b
# division = lambda a, b: a / b if b!=0 else 'Ошибка!! На ноль делить нельзя'


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return 'Ошибка!! На ноль делить нельзя'
    else:
        return a / b

# print(add(3, 5))
# print(subtract(3, 5))
# print(multiplication(3, 5))
# print(division(3, 5))


print('Выберите операцию: ')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')

valid_choice = ['1', '2', '3', '4', '+', '-', '*', '/']
choice = None

while choice not in valid_choice:
    choice = input('Введите число от 1 до 4 или +,-,*,/: ')
    if choice not in valid_choice:
        print('Ошибка! Выбрана неправильная операция.')

# choice = input(
#     'Выберите операцию (сложение, вычитание, умножение или деление): ').lower()
num_1 = get_number('Введите первое число: ')
num_2 = get_number('Введите второе число: ')

if choice == '+' or choice == '1':
    print(f'Результат: {num_1} + {num_2} = {add(num_1, num_2)}')
elif choice == '-' or choice == '2':
    print(f'Результат: {num_1} - {num_2} = {subtract(num_1, num_2)}')
elif choice == '*' or choice == '3':
    print(f'Результат: {num_1} * {num_2} = {multiplication(num_1, num_2)}')
elif choice == '/' or choice == '4':
    result = division(num_1, num_2)
    if isinstance(result, str):
        print(result)
    else:
        print(f'Результат: {num_1} / {num_2} = {result:.2f}')
else:
    print('Ошибка! Выбрана неправильная операция.')
