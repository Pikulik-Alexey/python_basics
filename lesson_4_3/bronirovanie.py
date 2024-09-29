from tkinter import *
from tkinter import messagebox as mb


# инициализация функций
def book_seat(event=None):
    try:
        seat_name = seat_entry.get().upper()
        if seats[seat_name] == "свободно":
            seats[seat_name] = "забронировано"
            update_canvas()
            mb.showinfo("Успешно", f"Место {seat_name} успешно забронировано.")
        else:
            mb.showerror(
                "Ошибка", f"Место {seat_name} уже забронировано или не существует.")

    except KeyError:
        mb.showerror("Ошибка", f"Место {seat_name} не существует.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


def update_canvas():
    canvas.delete("all")
    for i, (seat, stat) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if stat == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)


window = Tk()
window.title("Бронирование мест")
window.geometry("400x200")

canvas = Canvas(width=400, height=100)
canvas.pack()

# основной код
seats = {f'Б{i}': "свободно" for i in range(1, 10)}


seat_entry = Entry()
seat_entry.pack()
seat_entry.bind("<Return>", book_seat)

Button(text="Забронировать", command=book_seat).pack(pady=10)

update_canvas()

window.mainloop()

