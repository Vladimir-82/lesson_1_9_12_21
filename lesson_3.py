# n = str(input('input name:'))
#
# print(f'Привет, {n}')
# print(f'Привет, {n * 3}')
# print(f'Привет, {n} {n} {n}', sep=' ')

# string = 'hello'

# if len(string) > 3:
#     print(string[::3])
#     print(string[0] + string[-1])
#     print(string.upper())
#     print(string[::-1])
#     print(string.isdigit())

string = 'на ворован   '
strp = string.strip()
splt = strp.split(' ')
print(splt)

res = ''.join(splt)
print(res)

if res == res[::-1]:
    print('строка является полиндромом')
else:
    print('строка не является полиндромом')