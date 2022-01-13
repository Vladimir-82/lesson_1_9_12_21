dc = {'сардины': [5, 4], 'краб': [10, 3], 'анчоус': [20, 5], 'крокодил': [20, 5]}

for k, v in dc.items():
    print(k, v[0], v[1], sep='-')

n = int(input('Введите кол-во позиций:'))

price_to_pay = []
for i in range(n):
    good = input('Введите наименование товара:').lower()
    quantity = int(input('Введите колличество покупаемого товара:'))
    if good in dc:
        price_to_pay.append(dc[good][0] * quantity)
        dc[good][1] -= quantity
print(f'Вам стоит заплатить {sum(price_to_pay)} рублей')

for k, v in dc.items():
    print(f'Осталось-{k}-{v[1]} шт')