from math import pi
from random import randint
# pr = lambda x, y: x + y
#
# print(pr(3, 4))
# print(pr(5, 6))


# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
#
#
# print(mul(2)(3))

# wraper
# def first_test():
#     print('Test func 1')
#
# def second_test():
#     print('Test func 2')
#
#
# def simple_decore(fn):
#     def wraper():
#         print('some text')
#
#     fn()
#     print('stop function...')
#     return wraper
#
# f_1 = simple_decore(first_test)
# f_2 = simple_decore(second_test)
#
#
#
# def first_test():
#     print('Test func 1')
#
# def second_test():
#     print('Test func 2')

# decorator
# def param_tr(fn):
#     def surrog(args):
#         print('Some text')
#         fn(args)
#
#     return surrog
#
# @param_tr
# def print_sqrt(num):
#     print(num**2)
#
# print_sqrt(3)


# def func(a, b):
#     mass = [randint(a, b) for _ in range(10)]
#     print(mass)
#
# func(1, 10)


# def func(sec):
#
#     days, sec = divmod(sec, 3600 * 24)
#     hours, sec = divmod(sec, 3600)
#     minuts, sec = divmod(sec, 60)
#     return f'{days}:{hours}:{minuts}:{sec}'
#
# print(func(10000))


def func(x):

    if -5 <= x <= 5:
        print(x ** 2, end=' ')
    elif x < -5:
        print(2 * abs(x) - 1, end=' ')
    else:
        print(2 * x, end=' ')


for el in range(-10, 10):
    func(el)