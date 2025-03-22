# class Human:
#     def __init__(self, name = None, age = 0):
#         self.name = name
#         self.age = age
#
# class Bus:
#     def __init__(self):
#         self.passenger = []
#
#     def Addpassenger(self, b: Human):
#         self.passenger.append(b)
#
#     def Allpassenger(self):
#        for i in self.passenger:
#            print(i.name)
#
# obj = Human()
# b = Bus()
# b.Addpassenger(obj)
# b.Allpassenger()

# class Book:
#     def __init__(self, title = None, author = None):
#         self.title = title
#         self.author = author
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def Addbook(self, a: Book):
#         self.books.append(a)
#
#     def Printbook(self):
#         for book in self.books:
#             print(book.title, book.author)
#
#     def Removebook(self, name):
#         for book in self.books:
#             if name == book.title:
#                 self.books.remove(book)
#
# x = Book("Укр. мова", "голуб")
# a = Library()
# a.Addbook(x)
# a.Printbook()
# a.Removebook("Укр. мова")
# a.Printbook()

# class Person:
#     def __init__(self, name = None, age = 0):
#         self.name = name
#         self.age = age
#
#     def Talk(self):
#         print("Привіт, я людина")
#
#     def PrintInfo(self):
#         print(f"name = {self.name}, age = {self.age}")
#
# class Taxist(Person):
#     def __init__(self, name = None, age = 0, snack = None):
#         super().__init__(name, age)
#         self.snack = snack
#
#     def Talk2(self):
#         print("Привіт, я таксист")
#
#     def PrintInfo(self):
#         super().PrintInfo()
#         print(f"snack = {self.snack}")
#
# a = Person("Мар'яна", 23)
# b = Taxist("Василь", 42, "цигари")
# a.PrintInfo()
# a.Talk()
# b.PrintInfo()
# b.Talk2()

# class Vehicle:
#     def __init__(self, brand = None, speed = 200):
#         self.brand = brand
#         self.speed = speed
#
#     def Info(self):
#         print(f" brand = {self.brand}, speed = {self.speed}")
#
# class Car(Vehicle):
#     def __init__(self, brand=None, speed=200, fuel = None):
#         super().__init__(brand, speed)
#         self.fuel = fuel
#
#     def Info(self):
#         super().Info()
#         print(f" fuel = {self.fuel}")
#
# a = Vehicle()
# b = Car()
# a.Info()
# b.Info()







# class Car:
#     def drive(self):
#         print("The car is driving")
#
# class Plane:
#     def fly(self):
#         print("The plane is flying")
#
# class FlyCar(Car, Plane):
#     def show_abilites(self):
#         super().drive()
#         super().fly()
#
#
# f = FlyCar()
# f.show_abilites()





















