import datetime

t = datetime.datetime.now()  # now позволяет получить текущую дату и время
print(f'Текущее время: {t}')

d = datetime.date.today() #today позволяет получить текущую дату
print(f'Текущая дата: {d}')

# Форматированная дата
# d = datetime.date.today()
date = d.strftime('%d.%m.%y')
print(f'Сегодня: {date}')
date = d.strftime('%d.%m.%Y')
print(f'Сегодня: {date}')  # полный год
date = d.strftime('%d %B %y')
print(f'Сегодня: {date}')
