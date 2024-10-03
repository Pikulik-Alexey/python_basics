# Сортировка по дате
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import shutil
from datetime import datetime


def choose_dir():
    directory = fd.askdirectory()
    if directory:
        organization_photo(directory)


def organization_photo(directory):
    for file in os.listdir(directory):
        if file.lower().endswith(('.jpg', '.png', '.jpeg', '.gif')):
            filepath = os.path.join(directory, file)
            timestamp = os.path.getmtime(filepath)
            date = datetime.fromtimestamp(timestamp)
            year_month = date.strptime('%Y_%m')
            new_directory = os.path.join(directory, year_month)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            shutil.move(filepath, os.path.join(new_directory, file))
    mb.showinfo('Информация', 'Фотографии успешно перемещены')


win = Tk()
win.withdraw()

choose_dir()
win.destroy()
win.mainloop()


# from tkinter import filedialog as fd
# from tkinter import messagebox as mb
# import os
# import shutil
# from datetime import datetime


# def choose_directory():
#     direc=fd.askdirectory(title="Выберите папку для сортировки")
#     if direc:
#         organize(direc)

# def organize(direc):
#     for file in os.listdir(direc):
#         if file.lower().endswith((".jpg",'.png')):
#             filepath=os.path.join(direc,file)
#             filestamp=os.path.getmtime(filepath)
#             date=datetime.fromtimestamp(filestamp)
#             y_m=date.strftime("%Y%m")
#             new_dir=os.path.join(direc,y_m)
#             if not os.path.exists(new_dir):
#                 os.makedirs(new_dir)
#             shutil.move(filepath,os.path.join(new_dir, file))
#     mb.showinfo("Готово","Файлы успешно отсортированы.")
# choose_directory()
