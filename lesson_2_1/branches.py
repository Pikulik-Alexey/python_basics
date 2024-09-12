# if, elif, else

n = input('Введите число: ')
print(n)

if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
    n = int(n)
    if n < 0:
        print('Число отрицательное')
    elif n > 0:
        print('Число положительное')
    else:
        print('Число равно нулю')
else:
    print('Введено не число')
