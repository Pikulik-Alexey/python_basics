# Дана некоторая строка:
# 'abcdeabc'
# Получите сет ее символов:
# {'a', 'b', 'c', 'd', 'e'}

s = 'abcdeabc'

# Вариант 1
print(set(s))

# Вариант 2

s_set = set()
for char in s:
    s_set.add(char)

print(s_set)
