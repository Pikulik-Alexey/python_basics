# Копирование изображений(или других форматов, которые указали)
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

win = Tk()
win.withdraw()

directory = fd.askdirectory(
    title='Выберите папку с изображениями для копирования')

if directory:
    new_directory = directory + '_new'
    if not os.path.exists(new_directory):
        # Создаем папку для копирования
        os.makedirs(new_directory)
    else:
        print(f'Папка {new_directory} уже существует')
    # Копируем изображения из исходной папки в новую
    for file in os.listdir(directory):
        if file.lower().endswith(('.jpg', '.png', '.jpeg', '.gif')):
            source_file = os.path.join(directory, file)
            destination_file = os.path.join(new_directory, file)
            try:
                shutil.move(source_file, destination_file)
                print(f'Файл перемещен')
            except Exception as e:
                print(f'Ошибка при перемещения файла {file}: {e}')
    print('Все скопировано')
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
#         os.makedirs(new_dir)
#         for file in os.listdir(direc):
#             if file.lower().endswith(('.jpeg','.jpg','.png')):
#                 source_file=os.path.join(direc,file)
#                 dest_file=os.path.join(new_dir,file)
#                 try:
#                     shutil.move(source_file, dest_file)
#                     print(f"Файл {file} успешно перемещен.")
#                 except Exception as e:
#                     print(f"Произошла ошибка {e}")
#         print(f"Изобрания пермещены из папки {direc} в папку {new_dir}")
#     else:
#         print("Папка уже есть")
# else:
#     print("Папка не была выбрана.")

