# Бронирование билетов
from tkinter import *
from tkinter import messagebox as mb


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


def update_canvas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = 'green' if status == 'свободно' else 'red'
        canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
        canvas.create_text(x + 15, y + 15, text=seat)

# # Функция enumerate
# names = ['Алексей', 'Антон', 'Елена', 'Николай']
# for i, name in enumerate(names):
#     print(f'{i}')
#     print(f'{i}. {name}')


win = Tk()
win.title('Бронирование мест')
win.geometry('400x300')

canvas = Canvas(width=400, height=80)
canvas.pack(pady=10)
# Создаем словарь
seats = {f'Б{i}': 'свободно' for i in range(1, 10)}
# print(seats)
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind('<Return>', book_seat)

Button(text='Забронировать место', command=book_seat).pack(pady=10)

cansel_seat_entry = Entry()
cansel_seat_entry.pack(pady=10)
cansel_seat_entry.bind('<Return>', book_delete)
Button(text='Отмена бронирования', command=book_delete).pack(pady=10)

win.mainloop()
