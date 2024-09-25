from tkinter import *

a = 1


def change():
    global a
    a += 1
    metka['text'] = a
    # if a == 10:
    #     metka['text'] = 'Закончили'


window = Tk()
metka = Label(text='1', width=70, height=15)
metka.pack()
knopka = Button(text='Инкремент', width=70, height=10)
knopka.config(command=change)
knopka.pack()
window.mainloop()


# Смайлики
# a = 128512


# def change():
#     global a
#     a += 1
#     metka['text'] = chr(a)


# window = Tk()
# metka = Label(text=chr(a), font='Arial 64')
# metka.pack()
# knopka = Button(text='Следующий смайлик', width=70, height=10)
# knopka.config(command=change)
# knopka.pack()
# window.mainloop()
