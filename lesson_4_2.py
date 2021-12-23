# i = 1
# while i < 11:
#     print(i ** 2)
#     i += 1
#
# print([i**2 for i in range(1, 11)])

# i = 15
# while i > 0:
#     print(i)
#     i -= 1

# a = int(input())
# b = int(input())
#
# if a > b:
#     while True:
#         if b < 0:
#             print(b)
#             b += 1
# else:
#     while True:
#         if a < 0:
#             print(a)
#             a += 1

# a = float(input('input 1'))
# b = float(input('input 1'))
#
# operation = str(input('input operation'))
# while True:
#
#     if operation == '+':
#         print(f'Ответ: {a + b}')
#     if operation == '-':
#         print(f'Ответ: {a - b}')
#     if operation == '*':
#         print(f'Ответ: {a * b}')
#     if operation == '/':
#         if b == 0:
#             print('на 0 делить нельзя')
#         else:
#             print(f'Ответ: {a / b}')
#     if operation == '0':
#         break

arraw = [*range(1, 8)]
counter_odd = 0
counter_even = 0
for i in arraw:
    if i % 2:
        counter_odd += 1
    if not i % 2:
        counter_even += 1
if counter_even > counter_odd:
    print(sum(arraw))
else:
    print(arraw[0] * arraw[2] * arraw[5])

