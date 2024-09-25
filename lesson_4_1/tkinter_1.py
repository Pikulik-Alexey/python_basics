from tkinter import *


def change():
    # Замена текста и фона на новый
    metka['text'] = 'Привет, всему миру!'
    metka['bg'] = 'Black'


# Создание окна
window = Tk()

# Создание метки и запаковка, изменение фона, размер метки
metka = Label(window, text="Привет, мир!", bg='Red',
              fg='Green', width=70, height=15)
metka.pack()
# Добавление кнопки
knopka = Button(text='Изменить метку', width=70, height=10)
knopka.config(command=change)
knopka.pack()

window.mainloop()
# =================
