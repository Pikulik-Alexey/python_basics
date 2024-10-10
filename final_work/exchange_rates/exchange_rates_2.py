import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def exchange():
    # Получаем из поля ввода
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            # Запрашиваем курс обмена
            response = requests.get(
                f'https://open.er-api.com/v6/latest/{b_code}')
            # Проверяем статус
            response.raise_for_status()
            data = response.json()
            # Ищем курс для введенной валюты
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                # Выводим курс
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
            else:
                mb.showinfo('Ошибка', f'Валюта {t_code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


# Словарь кодов и названий валют

cur = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'GBP': 'Британский фунт',
    'JPY': 'Японская йена',
    'RUB': 'Российский рубль',
    'CHF': 'Швейцарский франк',
    'CAD': 'Канадский доллар',
    'AUD': 'Австралийский доллар',
    'CNY': 'Китайский юань',
    'INR': 'Индийская рупия',
    'KRW': 'Корейский вон',
    'MYR': 'Малайзийский ринггит',
    'NZD': 'Новозеландский доллар',
    'SGD': 'Сингапурский доллар',
    'THB': 'Тайский бат',
    'TRY': 'Турецкая лира',
    'ZAR': '��жно-Африканский рэнд'
}


# Создаем оконный интерфейс
win = Tk()
win.title('Курсы обмена валют')
win.geometry('360x360')

Label(text='Базовая валюта').pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text='Целевая валюта').pack(padx=10, pady=10)

# Создаем выпадающий список валют
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>', update_t_label)
# ================================

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена',
       command=exchange).pack(padx=10, pady=10)

win.mainloop()
