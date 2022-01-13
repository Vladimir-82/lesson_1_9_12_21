# ex1
# person = dict(name='Minsk', age=22, city='Minsk')
# for key in person:
#     print(person[key])
#
# print(person['age'])

# ex2
# cars = {'BMW': [310, 520, 750], 'Tesla': [53, 7566, 3]}
#
# print(cars['BMW'][1])
# print(cars['Tesla'][2])

# ex3
# d1 = {'a' :100, 'b' :200, 'c': 300}
# d2 = {'a' :300, 'b' :200, 'c': 400}
# print(d1['b'] == d1['b'])

# ex4
# d1 = {'a': 100, 'b': 200, 'c': 300}
# print(d1['a'] * d1['b'] * d1['c'])
# mult = 1
# for k in d1:
#     mult *= d1[k]
# print(mult)

# ex_5

# print(dict(zip([1, 2, 3], [4, 5, 6])))
dc = 'pythonist'

print(list(map(lambda x: 'pythonist'.count(x), list('pythonist'))))
print({i: dc.count(i) for i in dc})
