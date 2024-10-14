# Дан список с числами:
# [1, 2, 3, 4, 5, 6]
# Увеличьте каждое число из списка на 10 процентов.

s = [1, 2, 3, 4, 5, 6]
for i in range(len(s)):
    s[i] *= 1.10

print(s)
my_formatted_list = ['%.2f' % elem for elem in s]
print(my_formatted_list)
