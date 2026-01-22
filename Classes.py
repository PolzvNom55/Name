'''Классы и объекты'''
class Car:
    def __init__(self, name, years):
        self.name = name
        self.years = years
    def get_info(self):
        return self.name, self.years
c = Car('Toyota Camry', 2008)
print(c.get_info())


#1:
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price =  price
    def get_info(self):
        return ["Telephone:",self.brand], ["Модель:",self.model], ['Цена:', self.price]
P = Phone('Samsung', 10, 20000)
print(P.get_info())

#2:
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def get_description(self):
        return 'Фильм:', self.title, 'Режиссер:', self.director, 'Год выпуска:', self.year
m = Movie('Films', 'Ivan', 2004)
print(set(m.get_description())) 

#3:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return 'Площадь:', self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
rect = Rectangle(5, 10)
print(rect.area()) #Площадь
print(rect.perimeter()) #Периметр
 
#4:
class Teacher:
    def __init__(self, name, subject, experiense):
        self.name = name
        self.subject = subject
        self.experiense = experiense
    def info(self):
        return 'Имя:', self.name, 'учитель предмета:', self.subject, 'с опытом:', self.experiense
p = Teacher('Vanya', 'Math', 10)
print(p.info())

# 5:
class ShopCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"'{item}' добавлен в корзину")

    def remove_item(self):
        if item in self.items:
            self.items.remove(item)
            print(f"'{item}'удален из корзины")
        else:
            print(f"'{item}'нет в корзине")

    def total_items(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        print("Корзина очищена")
    
cart = ShopCart()
cart.add_item('apple')
cart.add_item('Bread')
cart.clear()
print(f'Товаров после очистки: {cart.total_items()}')



class Settings:
    def __init__(self, data_file, app_file):
        self.data_file = data_file
        self.app_file = app_file
    def nazvanie(self):
        return ('Главный файл:', self.data_file, 'Загружечный файл:', self.app_file)
sts = Settings('Файл Базы Данных - 1.8', 'Версия прошивки - 2.0')
print('Файловые настройки: ', sts.nazvanie())



