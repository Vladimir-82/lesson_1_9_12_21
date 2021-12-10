from random import randint as rand

# def func(arg):
#
#     arg = str(arg)
#     sum = 0
#     for i in arg:
#         sum += int(i)
#     return sum
#
# var = rand(100, 999)
# print('number:', var)
# print('sum =', func(var))


def func(arg):
    return sum([int(i) for i in str(arg)])

# def func(arg):
#     return sum(map(int, str(arg)))


#
#
var = rand(100, 999)
print('number:', var)
print('sum =', func(var))

# sum = ''
# first = rand(0, 9)
# sum += str(first)
# second = rand(0, 9)
# sum += str(second)
# third = rand(0, 9)
# sum += str(third)
# print(f'Sumory is', int(sum))


# https://docs.python.org/3/library/math.html
