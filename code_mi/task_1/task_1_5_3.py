# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
total = 0
for i in range(1, 101, 2):
    total += i
print(total)
