# res = []
# lst = [4, 6, 3, 7]
# lst_2 = [4, 7, 99, 100]
#
# for i in lst:
#     if i in lst_2:
#         res.append(i)
#
# print(res)


lst_1 = [4, 6, 1, 7, 'rtr', 'weww']
lst_2 = [4, 7, 99, 100]

lst = lst_1 + lst_2
lst.insert(3, 6)
print(lst)

for i in lst:
    if type(i) == str:
        lst.remove(i)

print(lst)
print(len(lst))