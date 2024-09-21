#  Создайте программу на Python, которая подсчитает сколько строк содержит название фирмы NEC, сколько SHARP и сколько SONY.

def word_search(text):
    firm = {'NEC': 0,
            'SHARP': 0,
            'SONY': 0}
    try:
        with open(text) as file:
            for line in file:
                # print(line)
                if 'NEC' in line:
                    firm['NEC'] += 1
                elif 'SHARP' in line:
                    firm['SHARP'] += 1
                elif 'SONY' in line:
                    firm['SONY'] += 1
            for i, j in firm.items():
                print(f"{i}: {j}")
    except FileNotFoundError:
        print('Файл не найден.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


# def firm_search():
#     firm = []
#     num = int(input('Сколько фирм будем искать? '))
#     for i in range(num):
#         word = input('Введите название фирмы(NEC/SHARP/SONY): ').upper()
#         if word == 'NEC' or word == 'SONY' or word == 'SHARP':
#             firm.append(word)
#         else:
#             print('Неверное название фирмы.')
#             word = input('Введите название фирмы(NEC/SHARP/SONY): ')
#     print(firm)
#     # return firm

# firm_search()
word_search('demo.log')
