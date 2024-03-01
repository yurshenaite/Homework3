coffee = input('цена в рублях, копейках, количество: ')
x, y, n = coffee.split(',')
x = int(x)
y = int(y)
n = int(n)
tr_k = ((x * 100) + y) * n
tr_r = tr_k // 100
ost_k = tr_k % 100
print(f'{tr_r} рублей {ost_k} копеек')