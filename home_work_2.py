# ex 3 calculator

num1 = float(input('Input first number: '))
operand = str(input('Input operand (+,-,*,/,//,%): '))
num2 = float(input('Input second number: '))

if operand == '+':
    print(f'Ответ: {num1 + num2}')
elif operand == '-':
    print(f'Ответ: {num1 - num2}')
elif operand == '*':
    print(f'Ответ: {num1 * num2}')
elif operand == '/':
    print(f'Ответ: {num1 / num2}')
elif operand == '//':
    print(f'Ответ: {num1 // num2}')
elif operand == '%':
    print(f'Ответ: {num1 % num2}')
else:
    print('Unknown operand')



# ex 4 function

# x = float(input('Введите x: '))
# if x > 0:
#     y = 2 * x - 10
# elif x == 0:
#     y = 0
# else:
#     y = 2 * abs(x) - 1
#
# print(f'y = {y}')



# ex 5 bool
# num1 = int(input('Input first number: '))
# num2 = int(input('Input first number: '))
#
# compear = (num1 > num2)
#
# if compear:
#     print(f'{num1} biger then {num2}')
# else:
#     print(f'{num1} not biger then {num2}')



# ex1 is leap year
'''
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400. ... Иными словами, если год делится на 4 без остатка, но делится на 100 только с остатком, то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный.
'''
# year = int(input('Input year: '))
#
# if (not year % 4 and year % 100) or not year % 400:
#     print(f'{year} is leap')
# else:
#     print(f'{year} is not leap')



# ex2 is triangle

# size_1 = float(input('Input first size: '))
# size_2 = float(input('Input second size: '))
# size_3 = float(input('Input third size: '))
#
#
# if size_1 + size_2 > size_3:
#     print('triangle is exists')
#     if size_1 == size_2 == size_3:
#         print('triangle is equilateral')
#     elif size_1 == size_2 or \
#             size_1 == size_3 or \
#             size_2 == size_3:
#         print('triangle is isosceles')
#
#     if size_1 ** 2 + size_2 ** 2 == size_3 ** 2 or size_1 ** 2 + size_3 ** 2 == size_2 ** 2 or size_2 ** 2 + size_3 ** 2 == size_1 ** 2:
#         print('triangle is rectangular')
#
# else:
#     print('triangle is not exists')



# ex3 point in the circle
# radius = float(input('Input radius of the circle: '))
# x = float(input('Input x: '))
# y = float(input('Input y: '))
#
# print('point in the circle' if x ** 2 + x ** 2 <= radius ** 2 else 'point not in the circle')


# ex4 password

'''
пароль доступа к сейфу состоит из трех равных частей, состоящих их трех символов. дверь будет открыта
только их последовательным вводом
'''
# key = '123456789'
# i = 1
# while key:
#     round = str(input(f'input {i} key: '))
#     if round == key[:3]:
#         key = key[3:]
#         i += 1
#     else:
#         print('Access is denied')
#         break
# if not key:
#     print('Welcome')


