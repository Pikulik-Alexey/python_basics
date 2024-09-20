# Работа с файлами

# try:
#     file = open('proba.txt', 'r', encoding='utf-8')
#     text = file.read()
#     print(text)
#     file.close()
# except FileNotFoundError:
#     print('Файл не найден')


# Вариант с with open
# try:
#     with open('proba.txt', encoding='utf-8') as file:
#         text = file.read()
#         print(text)
# except FileNotFoundError:
#     print('Файл не найден')

# # Перезапись файла
# file = open('proba2.txt', 'w', encoding='utf-8') #когда файл уже существукет, то в него перезаписывается текст, если файл не существует, то этот режим создает новый файл и записывает данные
# text = file.write('Малиновая ладабабабабабаб')
# file.close()

try:
    with open('proba2.txt', 'w', encoding='utf-8') as file:
        file.write("Некий текст.")
except IOError:
    print("Ошибка ввода-вывода.")
except OSError:
    print("Ошибка операционной системы.")
except UnicodeEncodeError:
    print("Ошибка кодирования текста.")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
