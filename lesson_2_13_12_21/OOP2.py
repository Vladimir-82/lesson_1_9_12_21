# class Car:
#
#     def __str__(self):
#         return 'Some text'
#
#
#     def stars(self):
#         print('wruuum')


#
#
#
# car = Car()
# car.stars()
# print(car)


class Human():
    default_name = 'Noname'
    default_age = 16

    def __init__(self, name=default_name, age=default_age):
        self.name = 'Vasia'
        self.age = 99
        self.__money = 1000
        self.__house = 'Villa'

    def info(self):
        return self.name, self.age, self.__house, self.__money


    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self):
        self.__money += 100

chell = Human()


chell.default_info()
print('_____________')

print(chell.info())
chell.earn_money()
print(chell.info())










