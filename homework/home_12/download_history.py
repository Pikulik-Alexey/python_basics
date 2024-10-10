from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import pyperclip
import json
import os


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status() 
                download_link = response.json()["link"]
                entry.insert(0, download_link)
                pyperclip.copy(download_link)
                save_history(filepath, download_link)
                mb.showinfo("Успешно!", "Ссылка успешно скопирована")
                entry.delete(0, END)
        else:
            raise ValueError("Не удалось отправить файл")

    except ValueError as v:
        mb.showerror("Ошибка", f"Произошла ошибка {v}")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


def save_history(file_path, download_link):
    hist_list = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            hist_list = json.load(file)

    hist_list.append({"file_path": os.path.basename(file_path),
                      "download_link": download_link})
    with open(history_file, "w") as file:
        json.dump(hist_list, file, indent=1)


def show_story():
    story_win = Toplevel(win)
    story_win.title("История загрузок")
    story_win.geometry("500x250+400+400")

    hist_list = []
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            hist_list = json.load(file)

    for el in hist_list:
        file_label = f"Файл: {el['file_path']}, Ссылка: {el['download_link']}"
        ttk.Label(story_win, text=file_label).pack(anchor='w')


history_file = "history.json"

win = Tk()
win.title("Файл в облако")
win.geometry("300x150+400+150")


upload_button = ttk.Button(text="Загрузить файл", command=upload)
upload_button.pack()

entry = ttk.Entry()
entry.pack()

story_button = ttk.Button(
    text="Посмотреть историю", command=show_story)
story_button.pack(pady=10)

win.mainloop()
