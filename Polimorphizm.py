'''Полиморфизм

Полиморфизм - это использование одного и того же метода в разных классах'''

# class Veek:
#     def move(self):
#         return 'колесо'
# class Car(Veek):
#     def move(self):
#         return 'Машина'
# class Boat(Veek):
#     def move(self):
#         return 'Лодка'
# class AirPlane(Veek):
#     def move(self):
#         return 'Самолет'

# car = Car()
# boat = Boat()
# airplane = AirPlane()

# print(car.move())
# print(boat.move())
# print(airplane.move())

'''Задание по теме:'''

#1:
class Animal:
    def make_sound(self):
        return 'Звуки'
class Dog(Animal):
    def make_sound(self):
        return 'звук собаки'
class Cat(Animal):
    def make_sound(self):
        return 'звук кота'

d = Dog()
c = Cat()

print(d.make_sound())
print(c.make_sound())
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 2:")

#2:
class Shape:
    def area(self):
        return 'Площадь фигур'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)

print(c.area())
print(r.area())
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 3:")

#3:
class Operation:
    def calculate(self, a, b):
        self.a = a
        self.b = b

class Addition(Operation):
    def calculate(self, a, b):
        print(f"{a} + {b} = {a + b}")

class Multiplication(Operation):
    def calculate(self, a, b):
        print(f"{a} - {b} = {a - b}")

class Subcration(Operation):
    def calculate(self, a, b):
        print(f"{a} * {b} = {a * b}")

class Division(Operation):
    def calculate(self, a, b):
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print('Ошибка: делить на 0 нельзя')

a, b = 10, 5
add = Addition()
sub = Subcration()
mul = Multiplication()
div = Division()

add.calculate(a, b)
sub.calculate(a, b)
mul.calculate(a, b)
div.calculate(a, b)
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 4:")

#4:
class Vihile:
    def move(self):
        pass
class Car(Vihile):
    def move(self):
        print('Машина едет')
class Bike(Vihile):
    def move(self):
        print('Мотоцикл едет')
class Boat(Vihile):
    def move(self):
        print('Лодка плывет')
c = Car()
b = Bike()
l = Boat()
c.move()
b.move()
l.move()
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 5:")

#5:
class Logger:
    def log(self, message):
        self.message = message

class ConsoleLogger(Logger):
    def log(self, message):
        print(f'печатает в консоль {message}')

class FileLogger(Logger):
    def log(self, message):
        print(f'записывает в файл {message}')

c = ConsoleLogger()
f =FileLogger()
c.log('привет')
f.log('привет')
print("-----------------------------------------------------------------------------------------------------------")
print('Задание 6:')

#6:
class Student:
    def get_grade(self):
        pass

class MathStudent(Student):
    def get_grade(self):
        print('Математика: 5')

class HistoryStudent(Student):
    def get_grade(self):
        print('История - 3')

class BiologyStudent(Student):
    def get_grade(self):
        print('Биология - 4')

s = MathStudent()
c = HistoryStudent()
b = BiologyStudent()

s.get_grade()
c.get_grade()
b.get_grade()
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 7:")

#7:
class CyrencyConverter:
    def convert(self, amount):
        pass

class USDConverter(CyrencyConverter):
    def convert(self, amount):
        converts = 80 #Dollar
        return amount * converts
    
class EURConverter(CyrencyConverter):
    def convert(self, amount):
        converts = 97 #Euro
        return amount * converts
    
usd = USDConverter()
eur = EURConverter()
print(usd.convert(10))
print(eur.convert(10))
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 8:")

#8:
class Shape:
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        print("Периметр квадрата = ", 4 * self.side)
        
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        print('Периметр треугольника = ', self.a + self.b + self.c) 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        print("Периметр круга = ", 2 * 3.14 * self.radius)

square = Square(5)
triangle = Triangle(3, 4, 5)
circle = Circle(7)

square.perimeter()
triangle.perimeter()
circle.perimeter()
print("-----------------------------------------------------------------------------------------------------------")
print("Задание 9:")

#9:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        print("Цена продукта =", self.price)

class Electronic(Product):
    def get_price(self):
        disc = self.price * 0.9
        print(f"Цена электроники с 10 % скидкой =", {disc})

class Clothings(Product):
    def get_price(self):
        disc = self.price * 0.8
        print(f"Цена одежды с 20 % скидкой =", {disc})
    
laptop = Electronic("ноутбук", 1000)
shift = Clothings("Футболка", 50)
laptop.get_price()
shift.get_price()








