from random import randint

# matrix = [
#     [1, 4, 5],
#     [-5, 8, 9]
# ]
#
# print(matrix)


# N = 3
# M = 2
# matrix = [[0] * M for j in range(N)]
# print(matrix)


# N = 3
# M = 2
# matrix = [[0] * M for j in range(N)]
# for i in range(N):
#     for j in range(M):
#         matrix[i][j] = randint(1, 9)
#         print(matrix[i][j], end=' ')
#     print()

# num = 4
# matrix = [
#     [1, 4, 5],
#     [-5, 8, 9]
# ]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if num == matrix[i][j]:
#             print(i, j)


# list1 = [1, 3, 0, 7]
#
# for i in list1:
#     try:
#         res = 2 / i
#         print(res ** 2)
#     except ZeroDivisionError:
#         print('Мы споймали исключение')
#
#     finally:
#         print('Код выполнен')
#         print('_________')



try:
    a = int(input())
    b = int(input())
    a / b
except ValueError:
    print('Ошибка значения')

except ZeroDivisionError:
    print('На 0 делить нельзя')

except Exception:
    print('Мы споймали исключение')
