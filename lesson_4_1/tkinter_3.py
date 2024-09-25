from tkinter import *

window = Tk()
frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

metka_1 = Label(frame_top, text='Метка 1', bg='red')
metka_1.pack(side=LEFT)
metka_2 = Label(frame_top, text='Метка 2', bg='green')
metka_2.pack(side=LEFT)
metka_3 = Label(frame_bottom, text='Метка 3', bg='yellow')
metka_3.pack(side=LEFT)
metka_4 = Label(frame_bottom, text='Метка 4', bg='blue')
metka_4.pack(side=LEFT)

window.mainloop()
