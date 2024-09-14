lst = [10, 25, 14, 11, 32, 21, 34, 42, 45, 67, 43, 32]
total = 0
length = len(lst)

for i in lst:
    total += i

average = total / length
print(f'Среднее арифметическое значение списка {lst} равно {average}')
print(f'Среднее арифметическое значение списка {lst} равно {total / len(lst)}')
