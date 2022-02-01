# ex1
def func(*args):
    """
    Определяет количество делителей для числа последовательности
    """
    for arg in args:
        counter = 0
        for el in range(1, arg + 1):
            if not arg % el:
                counter += 1
        print(f'Количество делителей для числа {arg} --> {counter}')


func(5, 2, 9, 7, 50)



# ex2
# def func(*args):
#     """
#     Находит в каждом числе последовательности
#     сумму четных цифр
#     """
#     for arg in args:
#         print(sum(map(int, filter(lambda x: not int(x) % 2, list(str(arg))))))
#
# func(12, 54, 444, 32, 24)



# ex3
# def func(*args):
#     """
#     Определяет являются ли цифры числа строго возростающей
#     последовательностью
#     """
#     for arg in args:
#         for num, el in enumerate(str(arg)):
#             if int(str(arg)[num + 1]) <= int(str(arg)[num]):
#                 print(f'Цифры числа {arg} не являются возростающей последовательностью')
#                 break
#             if num == len(str(arg)) - 2:
#                 print(f'Цифры числа {arg} являются возростающей последовательностью')
#                 break
#
#
# func(12, 54, 444, 32, 2489)



# ex4
from math import factorial

# def simple(arrow):
#     """
#     Определяет факториал каждого третьего простого
#     числа последовательности.
#     Рекурсию еще не проходили :)
#     """
#     simple = []
#     for arg in arrow:
#         for el in range(2, arg):
#             if not arg % el:
#                 break
#         else:
#             simple.append(arg)
#     print(f'Простые числа диапозона - {simple}')
#     [print(f'Число - {i}, его факториал - {factorial(i)}') for i in simple[::3]]
#
#
# n1, n2 = int(input()), int(input())
# simple(list(range(n1, n2)))



# ex5

# def func(number):
#     """
#     Проверяет изменилась ли разрядность числп после деления его на 2
#     """
#     return 'Изменилась' if len(str(number)) != len(str(number // 2)) else 'Не изменилась'
#
#
# print(func(70))
