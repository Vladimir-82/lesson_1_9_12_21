from random import randint as rand

# ex_1
# num = 12467
# lst = [int(i) for i in str(num)]
# even_numers = 0
# odd_numbers = 0
# for i in lst:
#     if i % 2:
#         odd_numbers += 1
#     else:
#         even_numers += 1
# if even_numers > odd_numbers:
#     print(sum(lst))
# else:
#     print(lst[0] * lst[2] * lst[5])

# ex_2
# vowels = 'aeiou'
#
# text = 'regegqee'
# counter_vowels = 0
# all_vowels = ''
# counter_consts = 0
#
#
# for i in text:
#     if i in vowels:
#         counter_vowels += 1
#         all_vowels += i
#     else:
#         counter_consts += 1
# print(f'Количество гласных - {counter_vowels}')
# print(f'Количество согласных - {counter_consts}')
# if counter_vowels == counter_consts:
#     print(all_vowels)


# ex_3
# input_num_1 = int(input())
# input_num_2 = int(input())
#
# count = 0
# for i in range(7):
#     random_num_1 = rand(1, 20)
#     random_num_2 = rand(1, 20)
#     if (input_num_1 + input_num_2) > (random_num_1 + random_num_2):
#         count += 1
# print(count)
# n = int(input('Введите количество чисел:'))
# seek = int(input('Введите искомое число:'))


# ex_4
# counter = 0
# for i in range(n):
#     num = rand(1000, 100000)
#     print(num)
#     if str(seek) in str(num):
#         counter += 1
# print(counter)


# ex_5
# string = 'df 4 92 lv!*'
# print([int(i) for i in string if i.isdigit()])

# ex_6
vowels = 'aeiou'
string = 'HjkLMeRvYYbb'
counter_vowels = 0
counter_consts = 0

for i in string:
    if i.lower() in vowels:
        counter_vowels += 1
    else:
        counter_consts += 1

print(f'Количество гласных - {counter_vowels}')
print(f'Количество согласных - {counter_consts}')
print(f'Букв в слове: {len(list(string))}')

upp_couple = 0
low_couple = 0
for i in range(len(string) - 1):
    if string[:2].islower():
        low_couple += 1
    if string[:2].isupper():
        upp_couple += 1

    string = string[1:]

print(f'Пар в верхнем регистре: {upp_couple}')
print(f'Пар в нижнем регистре: {low_couple}')




