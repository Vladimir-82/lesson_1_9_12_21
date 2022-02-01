# def add(x, y):
#     return x + y
#
# print(add(3, 3))


# def add(x, y):
#     return x + y
#     print('this function does not print')
#
# print('this string before func')
# print(add(4,5))
# print('this string after func')


# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
# print(add(2, 1))

# def fib(N):
#     a, b = 0, 1
#     for i in range(N):
#         print(a, end=' ')
#         a, b = b, a + b
# fib(15)


# def simple(arrow):
#     simple = []
#     not_simple = []
#     for el in arrow:
#         for i in range(2, el):
#             if el % i == 0:
#                 not_simple.append(el)
#                 break
#             simple.append(el)
#
#     print(min(simple))
#     print(max(not_simple))
#
# simple(list(range(5, 100)))


# так работает декоратор
# def func1(a):
#     def func2(b):
#         return a + b
#     return func2
#
# res = func1(2)
# print(res(3))
