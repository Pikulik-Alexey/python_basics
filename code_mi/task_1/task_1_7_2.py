# Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Найдите сумму квадратов элементов этого словаря.
total = 0
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
for i in my_dict.values():
    total += i ** 2
print(total)
