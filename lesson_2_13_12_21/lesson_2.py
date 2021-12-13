# x_1 = float(input('inp x1:'))
# y_1 = float(input('inp y1:'))
# x_2 = float(input('inp x2:'))
# y_2 = float(input('inp y2:'))
#
# k = (y_1 - y_2) / (x_1 - x_2)
# b = y_2 - k * x_2
# # y = k * x + b
# print(k, b)
# print(f'y = {k}x + {b}')

# var = int(input('Input namber:'))
# if var % 2:
#     print('odd namber')
# else:
#     print('even namber')

# a = int(input('input a'))
# b = int(input('input b'))
# c = input('input c')
#
# if a > 0 and b < 0:
#     print('and')
# elif a > 0 or b < 0:
#     print('or')
# if not c == False:
#     print('not')

a = int(input('input a:'))
b = int(input('input b:'))
c = int(input('input c:'))

maximum = a
if maximum < b:
    maximum = b

if maximum < c:
    maximum = c

print(maximum)
