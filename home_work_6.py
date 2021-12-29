vowels = 'aeiou'
arraw = [15, 48, 'hello', 6, 19, 'world']
arraw= [str(elem) for elem in arraw]
for elem in arraw:
    if elem.isalpha():
        counter_vowels = 0
        counter_consts = 0
        for letter in elem:
            if letter in vowels:
                counter_vowels += 1
            else:
                counter_consts += 1
        print(f'В слове {elem} гласных - {counter_vowels}. Согласных - {counter_consts}.')
    else:
        if int(elem) % 2:
            print(f'Число - {elem} - нечетное. Заменим его на 1')
            arraw[arraw.index(elem)] = 1
        else:
            print(f'Число {elem} четное. Сумма цифр числа = {sum([int(i) for i in list(elem)])}')
print(arraw)