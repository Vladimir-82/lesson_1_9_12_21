def ex_1(login, password, attempts=3,
         message='Система заблокирована. Повторите попытку через 5 минут.'):
    for attempt in range(1, attempts + 1):
        print(f'Попытка {attempt}')
        your_login = input('Введите логин: ')
        your_password = input('Введите пароль: ')
        if your_login == login and your_password == password:
            return 'Вы верифецированы!'
    else:
        return message

# print(ex_1(login='it', password='123'))


def ex_2(name, activity, born, dead=None):
    return f'{name} ({born} - {dead}) - {activity}' if dead != None else f'{name} ({born}) - {activity}'

# print(ex_2(name='Якуб Колас', born='03.11.1882', dead='13.08.1956', activity='Пісьменнік'))
# print(ex_2(name='Джоні Пустабрэх', born='03.11.1982', activity='Невядома хто'))




def count(num):
    return len(str(num))

def ex_3(*args):
    number_with_two_figures = 0
    number_with_three_figures = 0

    for arg in args:
        if count(arg) == 2:
            number_with_two_figures += 1
        if count(arg) == 3:
            number_with_three_figures += 1
    return f'В последовательности {number_with_two_figures} двухзначных чисел и {number_with_three_figures} трехзначных чисел'

print(ex_3(23, 456, 76, 543, 2, 888))

