# Вставка и удаление
from tkinter import *


def insert():
    pushkin = 'Я вас любил: любовь еще, быть может, \
    В душе моей угасла не совсем; \
    Но пусть она вас больше не тревожит; \
    Я не хочу печалить вас ничем. \
    Я вас любил безмолвно, безнадежно, \
    То робостью, то ревностью томим; \
    Я вас любил так искренно, так нежно, \
    Как дай вам Бог любимой быть другим.'
    t = text.insert(1.0, pushkin)


def delete():
    text.delete(1.0, END)


window = Tk()
text = Text(width=30, height=8, bg='black', fg='white')
text.pack(side=LEFT)
# Делаем скролл
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
# =================================================================
b_2 = Button(text='вставка текста', command=insert)
b_2.pack()
b_3 = Button(text='удаление текста', command=delete)
b_3.pack()
window.mainloop()
