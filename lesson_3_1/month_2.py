import datetime

t = datetime.date.today()
# ru = ''
m = t.month
s = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
     'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

month_ru = s[m - 1]

print(f'Сегодня {t.day} {month_ru} {t.year} года.')
