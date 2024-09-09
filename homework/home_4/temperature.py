temperature = input('Введите температуру: ')

if temperature.isdigit() or (temperature[0] == '-' and temperature[1:].isdigit()):
    temperature = int(temperature)
    if temperature < 0:
        print(f'Температура равна {temperature}. Озеро замерзло!!!!')
    elif 0 < temperature < 10:
        print(f'Температура равна {temperature}. Ледяная вода')
    elif 10 <= temperature < 15:
        print(f'Температура равна {temperature}. Жуть как холодно')
    elif 15 <= temperature < 18:
        print(f'Температура равна {temperature}. Прохладно, но можно купаться')
    elif 18 <= temperature < 24:
        print(f'Температура равна {temperature}. Вода кайф')
    elif 24 <= temperature < 30:
        print(f'Температура равна {temperature}. Полный кайф')
    elif 30 <= temperature < 36:
        print(f'Температура равна {temperature}. Горячая')
    elif temperature >= 36:
        print(f'Температура равна {temperature}. Кипяток')
    else:
        print(f'Температура равна {temperature}')
else:
    print(f'Введено некорректное значение температуры, равное {temperature}')
