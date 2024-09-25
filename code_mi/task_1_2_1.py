# Дано число. Выведите в консоль первую цифру этого числа.

num = int(input('Введите число: '))
print(num)
first_num = str(num)
print(int(first_num[0]))

# Второй вариант
while num >= 10:
    num = num // 10
print(num)
