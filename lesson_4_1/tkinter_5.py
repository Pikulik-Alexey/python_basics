# Многострочный ввод
from tkinter import *


def read():
    t = text.get(1.0, END)
    print(t)


window = Tk()
text = Text(width=30, height=8, bg='black', fg='white')
text.pack(side=LEFT)
# Делаем скролл
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
# =================================================================
b = Button(text='ввод', command=read)
b.pack()
b_2 = Button(text='вставка')
b_2.pack()
window.mainloop()


