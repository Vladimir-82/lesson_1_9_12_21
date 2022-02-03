# def func(*args):
#     res = []
#     for arg in args:
#         if not arg % 13 and arg > 0:
#             res.append(arg)
#     return max(res)
#
# print(func(26, 5, 77, 52, -39, -104))

# from math import pi
# def func(figure, a=None, b=None, d=None):
#       if figure == 'sq':
#           return a * a
#       if figure == 'rect':
#           return a * b
#       if figure == 'cirl':
#           return (pi * d ** 2) / 4
#
# fig = input('input figure:')
# if fig == 'sq':
#     squear_side = int(input('input squear_side:'))
#     print(func(fig, a=squear_side))
# elif fig == 'rect':
#     rect_side_1 = int(input('input first rectangle_side:'))
#     rect_side_2 = int(input('input second rectangle_side:'))
#     print(func(fig, a=rect_side_1, b=rect_side_2))
# elif fig == 'cirl':
#     diametr = int(input('input diametr:'))
#     print(func(fig, d=diametr))


# def cat_voice():
#     print('MEOW')
#
# def dog_voice():
#     print('WOOF')
#
# cat_voice()
# dog_voice()


# def cat_voice():
#     return 'MEOW'
#
# def dog_voice():
#     return 'WOOF'
#
# print(cat_voice() * 2)
# print(dog_voice() * 2)
#
# [print(i, end='') for i in cat_voice() * 2]

# def func(text):
#     return text + '!'
#
# print(func('erer'))


# def func(a, b):
#     return [i for i in range(a, b + 1) if i % 2]
#
# print(func(2, 9))

def func(*args):
    res = [i.lower() for i in args]
    if 'cat' in res:
        return True
    else:
        return False

print(func('feffe', 'gtrgtr', 'caT'))





