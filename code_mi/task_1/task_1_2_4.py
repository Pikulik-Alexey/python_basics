# Дано число. Выведите количество цифр в этом числе.
num = int(input('Введите число: '))
number = num #ко второму варианту
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# Второй вариант
number_1 = str(number)
print(len(number_1))
