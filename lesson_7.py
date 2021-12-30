from random import randint
# turp = tuple([randint(1, 100) for i in range(10)])
# print(turp)
# print(max(turp))
# print(min(turp))



# tup_1 = tuple([randint(0, 5) for i in range(10)])
# tup_2 = tuple([randint(-5, 0) for j in range(10)])
# tup_3 = tup_2 + tup_1
# print(tup_3)
# print(tup_3.count(0))


# tup = ('wew', 'rtr', 'trtr')
# print(', '.join(tup))

#4
A = tuple([randint(1, 10) for i in range(10)])
print(A)
B = tuple([randint(1, 10) for j in range(10)])
print(B)

if sum(list(A)) > sum(list(B)):
    print('Сумма больше в кортеже A')
else:
    print('Сумма больше в кортеже B')

print(f'Позиция минимум кортежа A - {A.index(min(A))}')
print(f'Позиция минимум кортежа B - {B.index(min(B))}')