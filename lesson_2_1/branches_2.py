s = input('Введите время года: ')
print(s)
s = s.lower()
print(s)
if s == 'лето':
    print(f'{s.capitalize()} - прекрасное время для отдыха на пляже')
elif s == 'осень':
    print(f'{s.capitalize()} - хорошее время для прогулок в парке')
elif s == 'зима':
    print(f'{s.capitalize()} - катаемся на лыжах')
elif s == 'весна':
    print(f'{s.capitalize()} - пробуждение природы')
else:
    print(f'{s} - это не время года')
