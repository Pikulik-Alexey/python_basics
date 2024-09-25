# Всплывающее окно askyesno
from tkinter import *
from tkinter import messagebox as mb


def check():
    answer = mb.askyesno(title='Вопрос', message='Передать сообщение?')
    if answer:
        s = e.get()
        e.delete(0, END)
        m['text'] = s


window = Tk()
e = Entry(width=30, bg='black', fg='white')
e.pack()
b = Button(text='Передать?', command=check)
b.pack()
m = Label(height=3)
m.pack()

window.mainloop()
