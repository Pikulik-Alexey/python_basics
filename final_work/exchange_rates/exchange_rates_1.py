# Конвертор валют
import requests
import json
from tkinter import *
from tkinter import messagebox as mb
import pprint  # для красивого вывода результата


# Результат получим с помощью запроса
result = requests.get('https://open.er-api.com/v6/latest/USD')

# Преобразуем ответ в JSON
data = json.loads(result.text)

# Выводим результат
p = pprint.PrettyPrinter(indent=4)  # 4 отступа
p.pprint(data)

