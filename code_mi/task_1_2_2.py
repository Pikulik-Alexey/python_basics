# Дано число. Выведите в консоль последнюю цифру этого числа.

num = int(input('Введите число: '))
print(num)
last_num = str(num)
print(int(last_num[-1]))

# Второй вариант

l_num = num % 10
print(l_num)
