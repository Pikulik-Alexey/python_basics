import random

# help(random) узнать информацию

m_1 = {'Халк', 'Тор', 'Супермен', 'Пантера', 'Доктор', 'Сокол'}
m_2 = {'Сильный', 'Быстрый', 'Ловкий', 'Умный', 'Меткий'}
# метод choise() не принимает множества, преобразуем в list
s_1 = random.choice(list(m_1))
s_2 = random.choice(list(m_2))

print(f'Имя супергероя: {s_2} {s_1}')
print(random.choice('akhfoidhgflk')) # можно и из строки