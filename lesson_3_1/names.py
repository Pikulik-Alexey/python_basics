import random

name = ['Платон', 'Люба', 'Никита', 'Даниил', 'Алексей']
profession = ['таксист', 'машинист', 'слесарь', 'ученик', 'повар', 'халявщик']
rnd_name = random.randint(0, len(name) - 1)
rnd_profession = random.randint(0, len(profession) - 1)
age = random.randint(5, 25)
print(
    f'Меня зовут {name[rnd_name]} мне {age} лет, я {profession[rnd_profession]}')
