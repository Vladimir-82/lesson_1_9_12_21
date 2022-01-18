# f = open('test.txt', 'w').write('f aa 2 4 5 r w')
#
# with open("test.txt") as file:
#     res = file.read().split()
#     print(sum(map(int, filter(lambda x: x.isdigit(), res))))

# digits = []
# string = []
# with open("test_2.txt") as file:
#     res = file.read().split()
#     for i in res:
#         if i.isdigit():
#             digits.append(int(i))
#         else:
#             string.append(i)
#     digits.sort()
#     sort_str = sorted(string, key=len)
#
#     print(digits + sort_str)

while True:
    string = input()
    open('test_3.txt', 'w+').write(string)
    if string == '':
        break
with open("test_3.txt") as file:
    res = file.read()
    print(res)