# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.

num = int(input('Введите число: '))
num_1 = num #ко второму варианту
l_num = num % 10

while num >= 10:
    num = num // 10

total = num + l_num
print(total)

# Второй вариант
sum_num = str(num_1)
print(int(sum_num[0]) + int(sum_num[-1]))
