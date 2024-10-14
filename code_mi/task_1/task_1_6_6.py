# Дана некоторая строка:
# 'abcde'
# Переберите и выведите в консоль по очереди все символы с конца строки.
s = 'abcde'
s_1 = s[::-1]
for i in s_1:
    print(i)

# Можно также использовать реверсную функцию reversed()
# s_2 = reversed(s)
# for i in s_2:
    # print(i)

# for i in range(len(s)-1, -1, -1):
#     print(s[i])
