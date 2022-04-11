# 1) Создать класс Person c атрибутами first_name, last_name
# 2) Создать доп.класс Jack и наследовать его от Person , добавив при этом дополнительные атрибуты phone_number , balance 
# 3) Создать еще один класс Vito, который будет наследоваться от класса Jack :
#          у последнего класса должен быть дополнительный 1 метод:
#                  первый метод,который минусует от balance Jack n-число и плюсует это число к  Vito.balance

# # # Отправить дз через GitHub




class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Jack(Person):
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

human = Jack('Alina', 'Kim', '0703 000 ***', 1000)

class Vito(Jack):
    _n = 450

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def minus(self):
        a = human.balance - self._n
        b = self.balance + a
        print(b)

vito = Vito('Begi', 'Akylbekova', '0*** *** ***', 240)

Vito.minus(vito)