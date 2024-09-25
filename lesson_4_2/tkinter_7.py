# Ращмещение и размер главного окна (геометрия)
from tkinter import *

window = Tk()
window.title('Главное окно')
# Задание размера окна(400x400 в пикселях) и расположения(+250+150 По оси X и по оси Y)
# window.geometry('400x400+250+150')
# Расположение окна по центру
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
# print(f'Размер вашего монитора {w} на {h} пикселей')
w_2 = w // 2 - 200
h_2 = h // 2 - 200
window.geometry(f'400x400+{w_2}+{h_2}')
window.mainloop()
