# Дан словарь с числами:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Увеличьте каждое число из словаря в 2 раза:
# {
# 	'a': 2,
# 	'b': 4,
# 	'c': 6,
# 	'd': 8,
# }

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

for key, value in my_dict.items():
    my_dict[key] = value * 2

print(my_dict)
