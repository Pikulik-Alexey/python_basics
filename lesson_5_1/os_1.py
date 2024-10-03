from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime


win = Tk()
win.withdraw()

directory = fd.askdirectory()

# Выбор папки из директории
if directory:
    for file in os.listdir(directory):
        # Выбор только фотографий по расширению
        if file.lower().endswith(('.jpg', '.png', '.jpeg', '.gif')):
            # print(file)
            # Выводим дату создания файлов
            filepath = os.path.join(directory, file)
            lt = os.path.getatime(filepath)
            print(lt)
            # Переводим в нормальное время
            ft = datetime.fromtimestamp(lt).strftime('%d.%m.%Y')
            print(ft)


win.mainloop()


# from tkinter import *
# from tkinter import filedialog as fd
# import os
# from datetime import datetime


# window=Tk()
# window.withdraw()#спрятали главное окно

# directory=fd.askdirectory(title="Вы берите папку с картинками")#при открытии окна можно выбрать заголовок
# if directory:
#     print(directory)
#     for f in os.listdir(directory):#получаем названия файлов выбранной папки
#         if f.endswith((".jpg",".png",".gif")):#выводим только файлы определенных форматов
#             filepath=os.path.join(directory,f)
#             lt=os.path.getmtime(filepath)#получили время последнего изменения в секундах(миллиарды секунд)
#             ft=datetime.fromtimestamp(lt)#преобразовали миллиарды секунд в понятную дату
#             print(f"{f} - последнее изменения: {ft}")
