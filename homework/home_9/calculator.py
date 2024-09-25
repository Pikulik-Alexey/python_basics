from tkinter import *
from tkinter import messagebox as mb


def add():
    n_1 = num_1_e.get()
    if not n_1.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_2 = num_2_e.get()
    if not n_2.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_3 = num_3_e.get()
    if not n_3.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    b_add['text'] = 'Кнопка нажата!'
    b_add['width'] = 20
    b_add['bg'] = 'yellow'
    number_1, number_2, number_3 = int(n_1), int(n_2), int(n_3)
    result = number_1 + number_2 + number_3
    result_info['text'] = f'{number_1} + {number_2} + {number_3} = {result}'
    answer = mb.askokcancel('Информация', 'Еще будем проводить операции?')
    if answer:
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        b_add['text'] = 'Сложение'
        b_add['width'] = 10
        b_add['bg'] = 'grey'
    else:
        win.destroy()


def subtract():
    n_1 = num_1_e.get()
    if not n_1.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_2 = num_2_e.get()
    if not n_2.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_3 = num_3_e.get()
    if not n_3.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    b_sub['text'] = 'Кнопка нажата!'
    b_sub['width'] = 20
    b_sub['bg'] = 'yellow'
    number_1, number_2, number_3 = int(n_1), int(n_2), int(n_3)
    result = number_1 - number_2 - number_3
    result_info['text'] = f'{number_1} - {number_2} - {number_3} = {result}'
    answer = mb.askokcancel('Информация', 'Еще будем проводить операции?')
    if answer:
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        b_sub['text'] = 'Сложение'
        b_sub['width'] = 10
        b_sub['bg'] = 'grey'
    else:
        win.destroy()


def multiplication():
    n_1 = num_1_e.get()
    if not n_1.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_2 = num_2_e.get()
    if not n_2.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_3 = num_3_e.get()
    if not n_3.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    b_mult['text'] = 'Кнопка нажата!'
    b_mult['width'] = 20
    b_mult['bg'] = 'yellow'
    number_1, number_2, number_3 = int(n_1), int(n_2), int(n_3)
    result = number_1 * number_2 * number_3
    result_info['text'] = f'{number_1} * {number_2} * {number_3} = {result}'
    answer = mb.askokcancel('Информация', 'Еще будем проводить операции?')
    if answer:
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        b_mult['text'] = 'Сложение'
        b_mult['width'] = 10
        b_mult['bg'] = 'grey'
    else:
        win.destroy()


def division():
    n_1 = num_1_e.get()
    if not n_1.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_2 = num_2_e.get()
    if not n_2.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    n_3 = num_3_e.get()
    if not n_3.lstrip('-').isdigit():
        mb.showinfo('Ошибка', 'Введено не число!!!')
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        return
    b_div['text'] = 'Кнопка нажата!'
    b_div['width'] = 20
    b_div['bg'] = 'yellow'
    number_1, number_2, number_3 = int(n_1), int(n_2), int(n_3)
    if number_1 == 0 or number_2 == 0 or number_3 == 0:
        mb.showinfo('Ошибка', 'На ноль делить нельзя!!!')
        answer = mb.askokcancel('Информация', 'Еще будем проводить операции?')
        if answer:
            num_1_e.delete(0, END)
            num_2_e.delete(0, END)
            num_3_e.delete(0, END)
            b_div['text'] = 'Сложение'
            b_div['width'] = 10
            b_div['bg'] = 'grey'
        else:
            win.destroy()
            return
    else:
        result = number_1 / number_2 / number_3

    result_info['text'] = f'{number_1} / {number_2} / {number_3} = {result}'
    answer = mb.askokcancel('Информация', 'Еще будем проводить операции?')
    if answer:
        num_1_e.delete(0, END)
        num_2_e.delete(0, END)
        num_3_e.delete(0, END)
        b_div['text'] = 'Сложение'
        b_div['width'] = 10
        b_div['bg'] = 'grey'
    else:
        win.destroy()


win = Tk()
frame_top = Frame(win)
frame_top.pack()
frame_grid = Frame(win)
frame_grid.pack()
win.title('Калькулятор')
win.geometry('800x400+200+200')
info = Label(frame_top, text='Введите 3 целых числа', font='arial 14 bold')
info.pack()
info_num_1 = Label(frame_grid, text='Введите первое число: ',
                   font='arial 12 bold')
info_num_1.grid(row=0, column=0)
info_num_2 = Label(frame_grid, text='Введите второе число: ',
                   font='arial 12 bold')
info_num_2.grid(row=1, column=0)
info_num_2 = Label(frame_grid, text='Введите третье число: ',
                   font='arial 12 bold')
info_num_2.grid(row=2, column=0)
num_1_e = Entry(frame_grid, bg='gray',
                cursor='hand1', justify='center', font='arial 12 bold')
num_1_e.grid(row=0, column=1)
num_2_e = Entry(frame_grid, bg='gray',
                cursor='hand1', justify='center', font='arial 12 bold')
num_2_e.grid(row=1, column=1)
num_3_e = Entry(frame_grid, bg='gray',
                cursor='hand1', justify='center', font='arial 12 bold')
num_3_e.grid(row=2, column=1)

b_add = Button(frame_grid, text='Сложение',
               cursor='hand2', width=10, bg='grey', command=add)
b_add.grid(row=5, column=0, ipady=10, pady=10)
b_sub = Button(frame_grid, text='Вычитание',
               cursor='hand2', width=10, bg='grey', command=subtract)
b_sub.grid(row=6, column=0, ipady=10)
b_mult = Button(frame_grid, text='Умножение',
                width=10, bg='grey', cursor='hand2', command=multiplication)
b_mult.grid(row=5, column=1, ipady=10)
b_div = Button(frame_grid, text='Деление', width=10, bg='grey',
               cursor='hand2', command=division)
b_div.grid(row=6, column=1, ipady=10)

result_info = Label(height=3, fg='red', font='arial 30 bold')
result_info.pack()


win.mainloop()
