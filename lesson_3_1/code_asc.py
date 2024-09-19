# Коды АСКИ
for i in range(256):
    print(f'Символ {chr(i)}\tкод символа {i}')
print(ord('A'))

alf = 'abcdefghijklmnopqrstuvwxyz'
for i in alf:
    print(f'Код символа {i} - {ord(i)}')
print('-' * 30)
smile = '▓▒░(°◡°)░▒▓'
for j in smile:
    print(f'Код символа {j} - {ord(j)}')
print('-' * 30)
print(smile[3:8])  #срезы повтор
