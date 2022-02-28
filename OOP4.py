# class Fly():
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def can_fly(self):
#         print('I can fly')
#
#
# class Dug(Fly):
#
#     def can_fly(self):
#         super().can_fly()
#         print('I can fly. Im dug')
#
#
# class Aircraft(Fly):
#
#     def can_fly(self):
#         super().can_fly()
#         print('I can fly. Im aircraft')
#
#
# dug = Dug('Donald')
# print(dug)
# dug.can_fly()
# print('_____________')
#
# aircraft = Aircraft('Mria')
# print(aircraft)
# aircraft.can_fly()




# class Car():
#     def __init__(self, model):
#         self.model = model
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2018
#         else:
#             self.__model = model
#
#     def get_car_model(self):
#         return 'Год выпуска модели - ' + str(self.model)
#
# car_1 = Car(1921)
# print(car_1.get_car_model())
#
# car_2 = Car(2002)
# print(car_2.get_car_model())
#
#
# car_3= Car(2052)
# print(car_3.get_car_model())

import string
LETTERS_eng = string.ascii_lowercase
LETTERS_blr = 'абвгд'

class Alphabet():
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class AlphabetEng(Alphabet):
    __letters_num = 26


    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self.__class__.__letters_num

    @staticmethod
    def examle():
        print('Django framework')

obj_2 = AlphabetEng('eng', LETTERS_eng)
print(obj_2.is_en_letter('s'))

print(obj_2.letters_num())
AlphabetEng.examle()
print(__name__)


# obj = Alphabet('blr', LETTERS_blr)
# obj.print_()
# print(obj.letters_num())


