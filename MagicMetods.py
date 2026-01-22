'''Магические методы - самые нужные, (не все есть)'''

class Magic:
    def __init__(self, value):
        self.value = value 
        print("__init__ вызван")

    def __str__(self):
        print("__str__ вызван")
        return f"MAgic({self.value})"

    def __repr__(self):
        print("__repr__")
        return f"Magic(value={self.value})"
    
    def __len__(self):
        print("__len__ вызван")
        return len(self.value)
    
    def __bool__(self):
        print("__bool__ вызван")
        return self.value > 0
    
    def __eq__(self, other):
        print("__eq__ вызван")
        return self.value == other.value
    
    def __hash__(self):
        print("__hash__ вызван")
        return hash(self.value)
    
    def __getitem__(self, index):
        print("__getitem__ вызван")
        return self.value[index] 
    
    def __setitem__(self, index, val):
        print("__setitem__ вызван")
        self.value[index] = val

    def __contains__(self, item):
        print("__contains__ вызван")
        return item in self.value
    
    def __add__(self, other):
        print("__add__ вызван")
        return self.value + other.value
    
    def __call__(self):
        print("__call__ вызван")
        return "Объект вызван как функция"
        
    
    
            

a = Magic(5)
print(a) # str
print(a.__repr__()) #repr

a = Magic([1, 2, 3])
print(len(a)) # len

a = Magic(1)
if a: #Bool
    print("True")
else:
    print("False")

b = Magic(5)
a == b # eq

s = {a} # hash
print(s)

lst = Magic([10, 20 , 30]) # getitem
print(lst[1])

lst[1] = 99
print(lst.value) # setitem


print(20 in lst) # contains


x = Magic(10)
c = Magic(20) # add
print(x + c)

print(a()) # call

