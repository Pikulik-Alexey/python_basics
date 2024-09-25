from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, encoding="utf-8") as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')


def delete():
    text.delete(1.0, END)


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(('TXT File', '*.txt'),
                       ('All Files', '*.*'),)
        )
        if file:
            with open(file, 'w', encoding="utf-8") as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')


window = Tk()
text = Text(width=30, height=8, bg='black', fg='white')
text.pack(side=LEFT)
# Делаем скролл
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
# =================================================================
b_2 = Button(text='Открыть файл', command=insert)
b_2.pack()
b_3 = Button(text='удаление текста', command=delete)
b_3.pack()
b_4 = Button(text='Схранение', command=save)
b_4.pack()
window.mainloop()
