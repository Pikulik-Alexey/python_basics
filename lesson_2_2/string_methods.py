# Методы строк
t = 'Это тестовая строка'
print(t.find('т'))  # find находит первую по ходу букву
# find с параметров 2, пропускает первое вхождение букы и выдает следующую
print(t.find('т', 2))
print(t.find('тест'))
print(t.find('ю'))  # если нет буквы то выдаст -1
# print(t.index('ю'))  # index выдаст ошибку если нет буквы
print(t.index('тест'))
p = 'в'
print(f'Подстрока "{p}" найдена в {t.find(p)} позиции')
