# num_set = {1,2,3,4,5}
# num_set.pop()
# print(num_set)

# ex1

# lst1 = [1, 2, 3, 2, 5, 6, 1]
# lst2 = set(lst1)
#
# if len(lst1) != len(lst2):
#     print('Повторения есть')
# else:
#     print('Повторений нет')

# ex2

# dc = {str(i): i for i in range(5)}
# dc['new'] = 99
# dc[(1,2)] = [55, 66]
# print(dc['3'])
# del dc['2']
# print()
# for k, v in dc.items():
#     print(k)


# ex3
set1 = set([1, 2, 3, 4, 5])
set2 = frozenset([4, 5, 6, 7, 8])

print(set1 | set2)
print(set1 & set2)

print(set1 - set2)
print(set2 - set1)

