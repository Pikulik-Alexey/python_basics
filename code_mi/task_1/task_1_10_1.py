# Дана строка:
# 'abcdef'
# Получите каждый второй символ этой строки:
# 'ace'

s = 'abcdef'
result = ''
for i in range(0, len(s), 2):
    result += s[i]
print(result)
print(s[::2])
