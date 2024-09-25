t = '                Это строка с лишними пробелами          '

# Удаление пробелов справа и слева
s = t.strip()
print(t)
print(s)

# Перевод букв в нижний регистр
q = 'Маша и Миша'
w = q.lower()
print(w)
print(q)

# Перевод букв в верхний регистр
r = 'Маша и Миша'
y = r.upper()
print(y)
print(r)

# Делает первую букву предложения заглавной
x = 'Маша и Миша'
z = x.capitalize()
print(z)
print(x)

# Метод startswith
g = 'LADA Granat'
print(g.startswith('LADA'))
if g.startswith('LADA'):
    print('это автомобиль марки "LADA"')

# Метод endswith
h = input('Введите расстояние: ')
if h.endswith('см'):
    print('Это расстояние в сантиметрах')
elif h.endswith('мм'):
    print('Это расстояние в миллиметрах')
elif h.endswith('км'):
    print('Это расстояние в километрах')
elif h.endswith('м'):
    print('Это расстояние в метрах')