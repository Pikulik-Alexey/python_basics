# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратных корней элементов этого списка.
import math

total = 0
s = [1, 2, 3, 4, 5]
for i in s:
    n = math.sqrt(i)
    total += n
print(round(total, 2))
