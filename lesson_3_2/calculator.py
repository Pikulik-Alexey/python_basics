# Калькулятор с функциями

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


choice = input(
    'Выберите операцию (сложение, вычитание, умножение или деление): ').lower()
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if choice == 'сложение' or choice == '+':
    print(f'Результат: {num_1} + {num_2} = {add(num_1, num_2)}')
elif choice == 'вычитание' or choice == '-':
    print(f'Результат: {num_1} - {num_2} = {subtract(num_1, num_2)}')
elif choice == 'умножение' or choice == '*':
    print(f'Результат: {num_1} * {num_2} = {multiplication(num_1, num_2)}')
elif choice == 'деление' or choice == '/':
    print(f'Результат: {num_1} / {num_2} = {division(num_1, num_2)}')
else:
    print('Ошибка! Выбрана неправильная операция.')
