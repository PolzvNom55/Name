''''''
class ServiceError(Exception): pass
class ActivateError(ServiceError): pass
class UsageError(ServiceError): pass
class PaymentError(ServiceError): pass


class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_activate = False
        self.usage_counter = 0
    def activate(self):
        pass
    def deactivate(self):
        pass
    def use(self):
        pass
    def get_info(self):
        pass


class SubscriptionService(Service):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.is_paid = False # Оплачено ли

    def pay(self):
        self.is_paid = True # Оплата сервиса 

    def activate(self):
        if self.is_paid: # Проверка - можно актиировать только если оплачено 
            self.is_activate = True
        else:
            pass

    def deactivate(self):
        self.is_activate = False # Выключаем сервис 

    def use(self):
        if self.is_activate: # Используем только если сервис активирован 
            self.usage_counter += 1 # Увеличиваем счетчик использования 
        else:
            pass

    

class StorageService(Service):
    def __init__(self, name, price, storage_limit):
        super().__init__(name, price)
        self.storage_limit = storage_limit
        self.used_space = 0 
        self.is_activate = True

    def activate(self):
        self.is_activate = True 

    def use(self, amount):
        if not self.is_activate:
            pass

        if self.used_space + amount <= self.storage_limit: 
            self.used_space += amount
            self.usage_counter += 1
        else:
            pass


class VpnService(Service):
    def __init__(self, name, max_uses):
        super().__init__(name, 0)
        self.is_activate = True
        self.is_blocked = False
        self.consecutive_uses = 0
        self.max_uses = max_uses

    def use(self):
        if not self.is_activate:
            pass

        if self.is_blocked:
            pass

        self.usage_counter += 1
        self.consecutive_uses += 1 
        if self.consecutive_uses > self.max_uses:
            self.is_blocked = True

    def deactivate(self):
        self.is_activate = False
        self.consecutive_uses = 0

    def activate(self):
        self.is_activate = True


class CloudFunctionService(Service):
    def __init__(self, name, price, max_cost):
        super().__init__(name, price)
        self.total_cost = 0
        self.max_cost = max_cost
        self.is_activate = True
        self.is_blocked = False

    def use(self):
        if not self.is_activate:
            pass
        if self.is_blocked:
            pass
        self.usage_counter += 1
        self.total_cost += self.price
        if self.total_cost >= self.max_cost:
            self.is_blocked = True

        
def crash_test():
    return 1 / 0

def main():
    services = [
        SubscriptionService("Netflix", 10), 
        StorageService("Google Drive", 100, 50),
        VpnService("MyVpn", 3),
        CloudFunctionService("Lamba", 2, 10)
    ]

    while True:
        print("\nМеню")
        print("1. Показать все сервисы")
        print("2. Активировать сервис")
        print("3. ИСпользовать сервис")
        print("4. Деактивироавать сервис")
        print('5. Текстовая ошибка')
        print("0. Выход")



        try:
            choice = input("Выберите действие: ")
            if choice == "0":
                break

            if choice == "1":
                for i in range(len(services)):
                    print(f"{i} - {services[i].get_info()}")
            elif choice in ["2", "3", "4"]:
                iNdex = int(input("Введите индекс сервиса: "))
                service = services[iNdex]

                if choice == "2":
                    service.activate()
                    print(f"{service.name}")

                elif choice == "3":
                    service.use()
                    print(f"{service.name}")

                elif choice == "4":
                    service.deactivate()
                    print(f"{service.name}")

            elif choice == "5":
                crash_test()

            else:
                print("Неверный выбор")




        except ValueError:
            print("ОШибка нужно ввести число")

        except ServiceError as e:
            print(f"Ошибка сервиса = {e}")
        
        except ZeroDivisionError:
            print("Текстовая критическая ошибка поймана")

        except Exception as e:
            print(f"Другая ошибка {e}")


if __name__ == "__main__":
    main()
''''''