degrees = int(input('Введите число градусов: '))
step = (24 * 60) / 360
minutes = step * degrees
hours = minutes // 60
print(f'{hours} часов, {minutes} минут')
