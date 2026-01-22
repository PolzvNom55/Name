'''Инкапсуляция'''

# class Operations:
#     def __init__(self, a, b, c):
#         self.a = a
#         self._b = b # Одно подчеркивание = Сигнал! Предупреждение - НЕ ТРОГАТЬ!
#         self.__c = c # Уже по настоящему запривачено.

# try:
#     add = Operations(10, 5, 9)
#     print(add._b)
#     print(add.a)
#     print(add.__c)
# except AttributeError:
#     print("Ошибка: нельзя вывести - Запривачено")
# else:
#     print("Сработал особый механизм! - Ошибок не найдено")
# finally: 
#     print("Программа успешно завершилась!")



class Operation:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b 
        self.__c = c

    @property
    def get_name(self): # Геттер - означает: Взять
        print("Геттер функция вызов!")
        return (
            self.__c, # __c - НЕЛЬЗЯ получить, является приватным! Но исключение если в коде есть Геттер
            self.a, 
            self._b
) # Добавляем в кортеж атрибуты 

    @get_name.setter # Сеттер - означает: Поставить. Но в коде оно изменяет значение 
    def get_name(self, value):
        if value < 0:
            print("Меньше 0 нельзя писать!")
        else:
            self.__c = value # Изменяем значение приватного атрибута на 7
           

o = Operation(1, 20, 2) 
o.get_name = 7
print(o.get_name)
    
'''----------------------------------------------------------------------------------------------------------------------------'''

class Bank:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, sets):
        if sets < 0:
            print("NO ZeroError")
        else:
            self.__balance = sets

b = Bank(100)

b.balance = 1000
print(b.balance)

b.balance = -1
print(b.balance)


print("-----------------------------------------------------------------------------------------------------------------------------------------")


# Задание №1
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            print("Имя не может  быть пустым")
        else:
            self.__name = value

p = Person("Noob")

p.name = "Bob"
print(p.name)
p.name = ""



# Задание №2

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass
    def getbalance(self):
        pass

class Student:
    
    
