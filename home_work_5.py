from random import randint
num = randint(1, 10)
print(num)
color_num = randint(1, 2)
if color_num == 1:
    color = 'красный'
else:
    color = 'черный'
print(color)
print('Попробуй угадай!!!')
for i in range(1, 6):
    print('$$$$$$$$$$$$$$')
    print(f'Попытка {i}')
    your_num = int(input('Введите Ваше число!!!: '))
    your_color = str(input('Введите Ваш цвет!!!: '))
    if your_num == num and your_color == color:
        print('Вы сорвали Джекпот!!!')
        break
    print('Пока не верно!')
else:
    print('_______________')
    print('Вы проиграли!!!')
    print(f'Загаданное число: {num}, цвет: {color}')