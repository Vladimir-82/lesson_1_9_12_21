# ex1
# matrix = [[3, 2, 2],
#           [1, 8, 3],
#           [1, 99, 3],
#           [4, 5, 6]
#           ]
# res = 0
# summ = sum(matrix[0])
# for i in range(len(matrix)):
#     if sum(matrix[i]) > summ:
#         summ = sum(matrix[0])
#         res = i
# print(res)


# ex2
value_1 = None
value_2 = None
while value_2 == 0 or type(value_1) != int or type(value_2) != int:
    try:
        value_1 = int(input('Input first number: '))
        value_2 = int(input('Input second number: '))
        res = value_1 / value_2

    except ZeroDivisionError:
        print('делить на 0 нельзя!')
    except ValueError:
        print('Должны быть цифры!')
    else:
        print('Обошлись без ошибок.')
        print(res)

