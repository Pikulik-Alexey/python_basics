# Бронирование билетов

# Генератор списка
# seats = [i ** 3 for i in range(10)]
# seats = [[] for i in range(10)]
# seats = [i for i in range(10)]
# print(seats)

# a = [7, 4, 5, 6, 7]
# seats = [i for i in a]
# print(seats)

seats = [(f'Б{i}', 'свободно') for i in range(1, 10)]
# print(seats)


def book_seat(seats):
    try:
        seat_name = input(
            'Введите место для бронирования билета(Б1-Б9) - ').upper()
        i = seats.index((seat_name, 'свободно'))
        seats[i] = (seat_name, 'забронировано')
        print(f'Место {seat_name} успешно забронировано')
    except ValueError:
        print(f'Место {seat_name} успешно уже забронировано')
    except Exception as e:
        print(f'Произошла неожиданная ошибка {e}')


while True:
    book_seat(seats)
    booking = input("Хотите забронировать еще одно место?(да/нет) ")
    if booking.lower().strip() != "да":
        break

print("Итоговое состояние бронирования: ")
for seat in seats:
    print(f"{seat[0]}: {seat[1]}")
