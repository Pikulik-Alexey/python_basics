# Будильник
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


t = 0
music = False


def set():
    global t
    rem = sd.askstring(
        "Время напоминания", 'Введете время напоминания в формате ЧЧ:ММ (в 24 формате)')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t = dt.timestamp()
            print(t)
            text = sd.askstring('Текст напоминания',
                                'Введите текст напоминания')
            label.config(
                text=f'Установленно время на {hour:02}:{minute:02} с текстом {text}')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    win.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text='Установить новое напоминание')


win = Tk()
win.title('Напоминание')
win.geometry('400x300')
label = Label(text='Установите напоминание')
label.pack(pady=10)
set_button = Button(text='Установить напоминание', command=set)
set_button.pack(pady=10)
stop_button = Button(text='Остановить музыку', command=stop_music)
stop_button.pack(pady=10)

check()  # Запускаем проверку каждые 10 секунд

win.mainloop()
