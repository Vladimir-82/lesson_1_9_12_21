class House():
    has_gas = False
    has_electro = True
    has_internet = True
    has_garden = False
    has_helipad = False

    def __init__(self, aria, price, rooms, windows, doors=1):
        self.aria = aria
        self._price = price
        self.rooms = rooms
        self.windows = windows
        self.doors = doors

    def create_discount(self, znizka):
        self.disc = self._price * znizka / 100
        return self.disc


    def final_price(self, persent=0):
        final_price = (self._price - self.create_discount(persent)) * self.aria
        print(f'final_price - {final_price}')

    def use(self):
        print('Жилплощадь абстрактная')

    def remount(self):
        print('Мы сделали ремонт!')
        self._price += 100

    def __str__(self):
        return f'Площадь - {self.aria}, Цена - {self._price},' \
               f' Комнат - {self.rooms}, Окон - {self.windows},' \
               f' Дверей - {self.doors}, Газ - {self.__class__.has_gas},' \
               f' Электричество - {self.__class__.has_electro}, ' \
               f' Интернет - {self.__class__.has_internet}, Сад - {self.__class__.has_garden},' \
               f' Вертолетная площадка - {self.__class__.has_helipad}'


class CountryHouse(House):
    has_internet = False

    def add_room(self):
        self.rooms += 1
        print('Комнат стало больше!')

    def use(self):
        super().use()
        print('Жилплощадь с садом')

    def create_garden(self):
        self.__class__.has_garden = True
        print('Мы выростили сад!')


class Flat(House):
    has_gas = True

    def use(self):
        super().use()
        print('Жилплощадь в многоэтажке')


class Penthouse(CountryHouse, Flat):
    has_internet = True
    has_gas = False


    def create_helipad(self):
        self.__class__.has_helipad = True
        print('Мы построили вертолетную площадку!')


print('Дом абстрактный')
house = House(aria=100, price=2000, rooms=2, windows=4)
house.final_price(persent=5)
print(house)
print('___________________________')

print('Дом с садом')
counry_house = CountryHouse(aria=200, price=1500, rooms=6, windows=6, doors=2)
counry_house.final_price()
print(counry_house)
counry_house.use()
counry_house.remount()
counry_house.add_room()
print(counry_house)
counry_house.final_price()
print('___________________________')


print('Квартира в многоэтажке')
flat = Flat(aria=70, price=2100, rooms=3, windows=5)
print(flat)
flat.use()
print('___________________________')


print('Пентхоуз')
penthouse = Penthouse(aria=120, price=2500, rooms=4, windows=6, doors=1)
print(penthouse)
penthouse.use()
penthouse.create_garden()
penthouse.create_helipad()
print(penthouse)
penthouse.final_price(persent=50)
print('___________________________')