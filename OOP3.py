# class GrandParent:
# 
#     def method(self):
#         print('call from GrandParent')
# 
# 
# class ParentOne(GrandParent):
# 
#     def method(self):
#         super().method()
#         print('call from ParentOne')
# 
# 
# class ParentTwo(GrandParent):
# 
#     def method(self):
#         super().method()
#         print('call from ParentTwo')
# 
# 
# class Child(ParentOne, ParentTwo, ):
# 
#     def method(self):
#         super().method()
#         print('call from Child')
# 
# 
# obj = Child()
# obj.method()
# print(obj.__class__.__mro__)  # так можно посмотреть в каком порядке будут искаться методы


# class Duck:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
#     def fly(self):
#
#         print('I can fly')
#
# d = Duck('fff', 45)
#
# class Plane(Duck):
#     def __init__(self):
#         super().__init__('Mria', 450)
#         self.model = 'Boing'
#         self.x = 0
#         self.y = 0
#
#     def fly(self):
#         self.x += 100
#         self.y += 200
#         print('I can fly fuster')
#
#
#
# plane = Plane()
#
# print(plane.name)
# print(plane.model)
# plane.fly()
#
# print(plane.x, plane.y)



class House():
    def __init__(self, aria, price):
        self.aria = aria
        self._price = price

    def create_discount(self, znizka):
        self.disc = self._price * znizka / 100
        return self.disc


    def final_price(self, d=10):
        if d != None:
            final_price = self._price * self.aria - self.create_discount(d) * self.aria

        else:
            final_price = self._price * self.aria
        print(f'final_price - {final_price}')


class CountryHouse(House):

    def create_garden(self):
        pass

    def ogorod(self):
        pass

    def add_room(self):
        pass

    def trash_room(self):
        pass

    def make_remont(self):
        pass

#добавить динам параметры: колвщ комнат, цвет стен, ко-во дверей, кол-во окон

class Flat(House, CountryHouse):
    pass

# наличие ванной, свет, газ, интернет - булевые значение


class room(Flat):
    pass





house = House(50, 1000)
house.final_price()





