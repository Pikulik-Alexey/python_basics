# Калькулятор складывает 3 числа
from tkinter import *
from tkinter import messagebox as mb


def add():
    s_1 = e_1.get()
    if not s_1.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'Введено не целое число!')
        return
    s_2 = e_2.get()
    if not s_2.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'Введено не целое число!')
        return
    s_3 = e_3.get()
    if not s_3.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'Введено не целое число!')
        return
    num_1, num_2, num_3 = int(s_1), int(s_2), int(s_3)
    result = num_1 + num_2 + num_3
    m_1['text'] = f'{num_1} + {num_2} + {num_3} = {result}'
    answer = mb.askretrycancel('Вопрос', 'Сложить еще 3 числа?')
    if answer:
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)
        m_1['text'] = ''
    else:
        window.destroy()


window = Tk()
window.title('Калькулятор')
m = Label(text='Введите 2 целых числа и нажмите на кнопку',
          height=3, font='bold')
m.pack()
e_1 = Entry(width=30, bg='black', fg='white')
e_1.pack()
e_2 = Entry(width=30, bg='black', fg='white')
e_2.pack()
e_3 = Entry(width=30, bg='black', fg='white')
e_3.pack()
b = Button(text='Сложить?', command=add)
b.pack()
m_1 = Label(height=3)
m_1.pack()

window.mainloop()
