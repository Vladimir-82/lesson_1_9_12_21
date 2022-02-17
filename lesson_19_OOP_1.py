# def greet(a):
#     def name(b):
#         return f'Hello, {a}, {b}'
#     return name
#
# print(greet('job')('vova'))


# class House():
#     name = 'Stalinka'
#
#     def __init__(self, sqare, roof, garage, q_rooms, q_doors):
#         self.sqare = sqare
#         self.roof = roof
#         self.garage = garage
#         self.q_rooms = q_rooms
#         self.q_doors = q_doors
#
#     def add_square(self):
#         self.sqare = self.sqare + 4
#
#     def __str__(self):
#         return self.garage
#
# house = House(200, 'true', 'true', 4, 2)
# flat = House(26, 'true', 'false', 2, 1)
#
# print(house.sqare)
#
# house.add_square()
#
# print(house.sqare)
#
# print(house.__hash__())
# print(house.__dict__)
#
#
#
# print(house.name)
# print(flat.name)
#
#
# print(house)

# class Example():
#     a = 2
#     b = 3
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def get(self):
#         self.e = 10
#         return self.e
#
#     def summ(self):
#         return self.a + self.b
#
#     def step(self):
#         return self.c ** self.d
#
# obj = Example(4, 5)
#
# print(obj.get())
# print(obj.summ())
# print(obj.step())


class Calc():
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def summ(self):
        return self.number_1 + self.number_2

    def minus(self):
        return self.number_1 - self.number_2

    def mult(self):
        return self.number_1 * self.number_2

    def dev(self):
        return self.number_1 / self.number_2

a, b = int(input('Input a:')), int(input('Input b:'))
obj = Calc(a, b)
operation = input('Input your operation: ')

if operation == '+':
    print(obj.summ())
elif operation == '-':
    print(obj.minus())
elif operation == '*':
    print(obj.mult())
elif operation == '/':
    print(obj.dev())
else:
    print('Unsupported operation')