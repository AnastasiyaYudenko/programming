month = int(input('Введите порядковый номер месяца:'))


def season(mon):
    if month == 6 or month == 7 or month == 8:
        return 'summer'
    elif month == 9 or month == 10 or month == 11:
        return 'autumn'
    elif month == 12 or month == 1 or month == 2:
        return 'winter'
    elif month == 3 or month == 4 or month == 5:
        return 'spring'
    else:
        'Такой месяц не найден'


result = season(month)
print(result)