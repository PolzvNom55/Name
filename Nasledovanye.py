class Device:
    def __init__(self, obrand, omodel, oyear):
        self.obrand = obrand
        self.omodel = omodel
        self.oyear = oyear
    def show_info(self):
        print(f"{self.obrand} {self.omodel} ({self.oyear})")

class Laptop(Device):
    def __init__(self, obrand, omodel, oyear, ram): 
        self.obrand = obrand
        self.omodel = omodel
        self.oyear = oyear
        self.ram = ram
    def run_program(self, program_name):
        print(f"Запуск программы {program_name} на {self.omodel}")

    # def obrand(self):  #Ошибка 
    #     print('бренд')  #Ошибка 
    # def omodel(self):  #Ошибка 
    #     print('model') #Ошибка 
    # def oyear(self):  #Ошибка 
    #     print('лет')  #Ошибка 
    # def run_program(self, program_name):  #Ошибка 
    #     print(f"Запуск программы {program_name} на {self.omodel}")  #Ошибка 

class Printer(Device):
    def __init__(self, obrand, omodel, oyear, is_color):
        self.obrand = obrand
        self.omodel = omodel
        self.oyear = oyear
        self.is_color = is_color
    def print_document(self, doc_name):
        print(f"Печать документа {doc_name} на принтере {self.omodel}")

l1 = Laptop('HP', 'EliteBook', 2020, 16)
p1 = Printer('Canon', 'LBP6030', 2019, False)

l1.show_info()
l1.run_program("Visual Studio Code")

print("---")

p1.show_info()
p1.print_document("Отчет.pdf")




