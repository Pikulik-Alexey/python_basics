# Телефонный справочник
contacts = {}


def input_contact():
    name = input('Введите имя: ')
    phone = input('Введите десятизначный номер телефона, начинающийся с 9: ')
    # phone[0] == '9' или так вместо phone.startswith('9')
    if len(phone) == 10 and phone.isdigit() and phone.startswith('9'):
        contacts[name] = phone
        print('Контакт успешно добавлен')
        print(contacts)
    else:
        print('Ошибка! Неверный номер телефона!')


def find_contact():
    name = input('Введите имя для поиска: ')
    print(contacts.get(name, 'Контакт не найден'))
    # if name in contacts:
    #     print(contacts[name])
    # else:
    #     print(f'Контакт "{name}" не найден!')


def delete_contact():
    name = input('Введите имя для удаления: ')
    if name in contacts:
        del contacts[name]
        print('Контакт успешно удален')
        print(contacts)
    else:
        print(f'Контакт "{name}" не найден!')


print('Выберите действие: ')
print('1. Добавить')
print('2. Найти')
print('3. Удалить')
print('4. Выйти')

while True:
    action = input('Введите число от 1 до 4: ')
    if action == '1':
        input_contact()
    if action == '2':
        find_contact()
    if action == '3':
        delete_contact()
    if action == '4':
        break
    else:
        print('Неверный ввод. Выберите 1, 2, 3 или 4: ')
