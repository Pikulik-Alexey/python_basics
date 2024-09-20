# Количество слов в файле
def count(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            content = file.read()
            word = content.split()
            return len(word)
    except FileNotFoundError:
        print('Файл не найден.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


worlds = count('proba.txt')
print(f"Количество слов в файле: {worlds}")
