# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратов элементов этого списка.
import math

total = 0
s = [1, 2, 3, 4, 5]
for i in s:
    n = math.pow(i, 2)
    total += n
    # total += i ** 2
print(total)
