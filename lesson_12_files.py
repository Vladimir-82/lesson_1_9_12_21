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


# file = open('test_3.txt', 'w+')
# while True:
#     string = input()
#     if string == '':
#         break
#     file.write(string + '\n')
# file.close()
#
# with open("test_3.txt") as file:
#     print(*file)


file = open('test_3.txt', 'r').readlines()
counter = 0
for num, string in enumerate(file):
    print(f'Число букв в строке {num + 1} - {len(string)}')
    counter += 1
print(f'Всего строк - {counter}')