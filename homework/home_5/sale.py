text = input(
    'Введите параментры автомобиля по примеру: LADA 2010г 205000км 450000руб ')
text.replace(' ', '\n')
make, year, mileage, price = text.split()
print(f'Марка автомобиля - {make}')
print(f'Год выпуска - {year}')
print(f'Пробег: {mileage}')
print(f'Цена: {price}')
