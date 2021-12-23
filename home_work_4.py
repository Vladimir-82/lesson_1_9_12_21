# ex_1

# mult = 1
# for i in range(1, 100):
#     if i % 2:
#         mult *= i
# print(mult)

# ex_2

# arrow = []
# for i in range(1, 500 + 1):
#     if not i % 5:
#         arrow.append(i)
# print(arrow)

# ex_3
# for i in range(1, 497):
#     if not i % 2:
#         print(i)

# ex_4

arrow = [2, 5, 7, 5, 6, 5, 1, 99, 9, 7, 8, 7]
res = []
for i in arrow:
    if arrow.count(i) > 2:
        res.append(i)
print(set(res))