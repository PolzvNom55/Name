#1: Что такое ООП?
#1: b) Подход программирорвания основанный на объектах 

#2: а) Инкапсуляция, б) полиморфизм, в) наследование, г) абстракция

#3; б) Возможность создавать класс на основе другого класса 

#4:  а) Сокрытие реализации и контроль доступа к данным 

#5: а) Возможность одному методу вести себя по разному для разных объектов

#6: б) Упрощение = оставляем важное скрываем лишнее

#7: б) ЛОвит и обрабатывает ошибки во время выполнения 

#8: б) Программа упадет с ошибкой

# Часть 2-
#1:
class Animal:
    def sound(self):
        return "some sound"
class Dog(Animal):
    def sound(self):
        return "Woof"
b = Animal()
a = Dog()
print(b.sound())
print(a.sound())

#2:
def make_sound(obj):
    obj.sound()
    return [Animal, Dog]
print(make_sound)


#3:
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#         return f"{self.__balance} увеличивается от {amount}"

#     def get_balance(self):
#         return self.__balance

# v = BankAccount(100)
# print(v.deposit())
# print(v.get_balance())


#4:
class Figure: # У фигуры есть площадь но мы не реализуем ее
    def __init__(self):
        pass

# 5:
# try:
#     a = (input("ВВедите число: "))
#     print(int(a))
# except: 
#     print("ВВедите число!")


#6:
# try:
#     n = int(input("Введите число 6 задание: "))
#     print(100 / n)
# except ValueError:
#     print("Ввели буквы!!!")
# except ZeroDivisionError:
#     print("НА ноль делить нельзя!!!!")
    


#7:
class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle
    def nasledie(self):
        return "РОдительски1"
class Car(Vehicle):
    def __init__(self, banana):
        self.banana = banana
    def nasled(self):
        return "банан"
class ElectricCar(Car):
    def __init__(self, ban):
        self.ban = ban
    def nasledovanye(self):
        return "бан"


object = ElectricCar(["100", "10", "1"])
print(object.nasledie())
print(object.nasled())
print(object.nasledovanye())

        
        
