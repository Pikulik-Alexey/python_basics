# Игра угадай число
from tkinter import *
from tkinter import messagebox as mb
import random


def check():
    s = int(e.get())
    rnd = random.randint(1, 5)
    if s == rnd:
        mb.showinfo(title='Результат', message='Ты угадал!')
    else:
        mb.showinfo('Результат', 'Неудача')
    answer = mb.askretrycancel('Вопрос', 'Загадать еще?')
    if answer:
        e.delete(0, END)
    else:
        window.destroy()


window = Tk()
window.title('Игра "Угадай число"')
m = Label(text='Введи число и нажми на кнопку.', width=40)
m.pack()
e = Entry()
e.pack()
b = Button(text='Угадать', command=check)
b.pack()
m_1 = Label(height=3)
m_1.pack()

window.mainloop()
