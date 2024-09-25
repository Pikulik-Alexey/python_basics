# Создание меню

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


def quit():
    window.destroy()


window = Tk()
window.title('Главное окно')
# window.geometry('200x200+250+150')
# Создаем меню
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть', command=insert)
filemenu.add_command(label='Новый', command=delete)
filemenu.add_command(label='Сохранить', command=save)
filemenu.add_separator()  # линия - разделитель
filemenu.add_command(label='Выход', command=quit)
mainmenu.add_cascade(label='Файл', menu=filemenu)


text = Text(width=80, height=20, bg='black', fg='white', wrap=WORD)
text.pack(side=LEFT)
# Делаем скролл
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
# =================================================================

window.mainloop()
