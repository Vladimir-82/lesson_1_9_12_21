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

print(ex_1(login='it', password='123'))