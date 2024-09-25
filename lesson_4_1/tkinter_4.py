from tkinter import *


def read():
    name = e.get()
    print(name)
    e.delete(0, END)


def read_2():
    city = x.get()
    print(city)
    x.delete(0, END)


window = Tk()
frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top .pack()
frame_bottom.pack()
m = Label(frame_top, text='Введите имя: ', bg='gray',
          fg='white', font='Courier 18 bold')
m.pack(side=LEFT)
e = Entry(frame_top, width=50, bg='gray', fg='white',
          font='Courier 18 bold', justify='center')
e.pack(side=LEFT)
b = Button(frame_top, text='Ввод', bg='gray', fg='white',
           font='Courier 18 bold', command=read)
b.pack(side=LEFT)
z = Label(frame_bottom, text='Введите город: ',
          bg='gray', fg='white', font='Courier 18 bold')
z.pack(side=LEFT)
x = Entry(frame_bottom, width=50, bg='gray',
          fg='white', font='Courier 18 bold', justify='center')
x.pack(side=LEFT)
c = Button(frame_bottom, text='Ввод', bg='gray', fg='white',
           font='Courier 18 bold', command=read_2)
c.pack(side=LEFT)
window.mainloop()
