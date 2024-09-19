import random

name = []
profession = []
names = int(input('Сколько имен введете? '))
professions = int(input('Сколько профессий введете? '))

for i in range(names):
    name.append(input('Введите имя '))
for i in range(professions):
    profession.append(input('Введите профессию '))

# print(name)
# print(profession)

rnd_name = random.randint(0, names)
rnd_profession = random.randint(0, professions)
age = random.randint(5, 25)
print(
    f'Меня зовут {name[rnd_name]} мне {age} лет, я {profession[rnd_profession]}')
