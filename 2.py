time = int(input('Введите время в секундах: '))
if 1 <= time <= 86400:
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = (time % 3600) % 60
    print(f'Время равно {hours} часов')
    print(f'{minutes} минут')
    print(f'{seconds} секунд')
else:
    print('Неправильный ввод')