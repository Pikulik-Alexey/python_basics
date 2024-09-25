# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
number_1 = num_1
number_2 = num_2


while num_1 >= 10:
    num_1 = num_1 // 10
while num_2 >= 10:
    num_2 = num_2 // 10

if num_1 == num_2:
    print(f'Первые цифры чисел {number_1} и {number_2} совпадают')
else:
    print(f'Первые цифры чисел {number_1} и {number_2} не совпадают')
