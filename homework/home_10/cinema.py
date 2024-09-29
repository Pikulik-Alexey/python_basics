# Бронирование билетов
from tkinter import *
from tkinter import messagebox as mb

total = 0


def book_seat(event=None):
    s = seat_entry.get().upper()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo('Успех', f'Место {s} успешно забронировано')
        else:
            mb.showinfo('Ошибка', f'Место {s} уже забронировано')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует')


def book_delete(event=None):
    s = cansel_seat_entry.get().upper()
    try:
        if seats[s] == 'забронировано':
            seats[s] = 'свободно'
            update_canvas()
            mb.showinfo('Успех', f'Бронь места {s} успешно отменена')
        else:
            mb.showinfo(
                'Ошибка', f'Место {s} не забронировано или не существует')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует')


def info_price():
    mb.showinfo('Цена', f'Цена билетов на места Б1-Б10 равно 500 рублей \
               Цена билетов на места Б11-Б30 равна 300 рублей \
               Цена билетов на места Б31-Б50 равна 100 рублей ')
    if info_price:
        question = mb.askyesno('Вопрос', 'Хотите купить билет?')
        if question:
            mb.showinfo('Успех', 'Воспользуйтесь полем для бронирования мест')
        else:
            mb.showinfo(
                'Ошибка', 'Спасибо, что воспользовались нашим сервисом!!! Приложение будет закрыто')
            win.destroy()


def book_cost():
    global total
    total = 0
    for seat, status in seats.items():
        if status == 'забронировано':
            if seat.lstrip('Б') in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                # if seat.startswith('B1') or seat.startswith('B2') or seat.startswith('B3') or seat.startswith('B4') or seat.startswith('B5') or seat.startswith('B6') or seat.startswith('B7') or seat.startswith('B8') or seat.startswith('B9') or seat.startswith('B10'):
                total += 500
            elif seat.lstrip('Б') in ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']:
                total += 300
            elif seat.lstrip('Б') in ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']:
                total += 100
    mb.showinfo('Итоговая стоимость',
                f'Стоимость всех забронированных мест: {total} рублей')


def update_canvas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        if 0 <= i <= 9:
            x = i * 40 + 20
            y = 20
            color = 'green' if status == 'свободно' else 'red'
            canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            canvas.create_text(x + 15, y + 15, text=seat)
        elif 10 <= i <= 19:
            x = (i * 40 + 20) - 400
            y = 70
            color = 'green' if status == 'свободно' else 'red'
            canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            canvas.create_text(x + 15, y + 15, text=seat)
        elif 20 <= i <= 29:
            x = (i * 40 + 20) - 800
            y = 120
            color = 'green' if status == 'свободно' else 'red'
            canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            canvas.create_text(x + 15, y + 15, text=seat)
        elif 30 <= i <= 39:
            x = (i * 40 + 20) - 1200
            y = 170
            color = 'green' if status == 'свободно' else 'red'
            canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            canvas.create_text(x + 15, y + 15, text=seat)
        elif 40 <= i <= 49:
            x = (i * 40 + 20) - 1600
            y = 220
            color = 'green' if status == 'свободно' else 'red'
            canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            canvas.create_text(x + 15, y + 15, text=seat)


win = Tk()
win.title('Бронирование мест в кинотеатре')
win.geometry('1000x900')

canvas = Canvas(width=500, height=280)
canvas.pack(pady=10)

canvas_info = Canvas(width=500, height=70)

canvas_info.pack(pady=10)
canvas_info.create_rectangle(20, 0, 70, 50, fill='green')
canvas_info.create_text(135, 25, text='Свободно', font='Courier')
canvas_info.create_rectangle(220, 0, 270, 50, fill='red')
canvas_info.create_text(345, 25, text='Забронировано', font='Courier')


seats = {f'Б{i}': 'свободно' for i in range(1, 51)}
# seats_price_500 = {f'Б{i}': 500 for i in range(1, 11)}
# seats_price_300 = {f'Б{i}': 300 for i in range(11, 31)}
# seats_price_100 = {f'Б{i}': 100 for i in range(31, 51)}
# print(seats_price_300)
# print(seats_price_500)
# print(seats_price_100)

update_canvas()

Button(text='Информация о цене билетов', command=info_price).pack(pady=10)

seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind('<Return>', book_seat)

Button(text='Забронировать место', command=book_seat).pack(pady=10)

cansel_seat_entry = Entry()
cansel_seat_entry.pack(pady=10)
cansel_seat_entry.bind('<Return>', book_delete)
Button(text='Отмена бронирования', command=book_delete).pack(pady=10)
Button(text='Итоговая стоимость', command=book_cost).pack(pady=10)


win.mainloop()
