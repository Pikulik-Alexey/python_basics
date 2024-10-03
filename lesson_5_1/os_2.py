# Копирование файлов
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

win = Tk()
win.withdraw()

directory = fd.askdirectory(title='Выберите папку для копирования')

if directory:
    new_directory = directory + '_new'
    if not os.path.exists(new_directory):
        try:
            shutil.copytree(directory, new_directory)
            print(
                f'Все содержимое папки {directory} скорировано в папку {new_directory}')
        except Exception as e:
            print(f'Ошибка при копировании: {e}')
    else:
        print(f'Папка {new_directory} уже существует')
else:
    print('Папка не была выбрана')
win.destroy()
win.mainloop()


# from tkinter import *
# from tkinter import filedialog as fd
# import os
# import shutil


# #window=Tk()

# direc=fd.askdirectory(title="Выберите папку для копирования")

# if direc:
#     new_dir=direc + "_new"#добавляем к новому названию папки окончание _new
#     if not os.path.exists(new_dir):#проверяем не создана ли еще папка
#         try:
#             shutil.copytree(direc,new_dir)#копируем все содержимое из direc в new_dir
#             print(f"Все содержимое из {direc} скопировано в{new_dir}.")
#         except Exception as e:
#             print(f"Произошла ошибка {e}")
#     else:
#         print(f"Папка {new_dir} уже существует")
# else:
#     print("Папка не была выбрана")
