# Угадай число с помощью библиотеки рандом
import random

n = random.randint(1, 20)
a = 0
while a != n:
    a = int(input('Угадай число: '))
print(f'Поздравляю! Вы угадали, это число {a}')
