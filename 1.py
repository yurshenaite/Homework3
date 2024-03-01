bitcoin = int(input('Введите стоимость биткоина в рублях: '))
bitcoin_3 = (bitcoin // 100) % 10
print(f'На третьей позиции справа находится число {bitcoin_3}')