class Worker:  
    
    def __init__(self, name, surname, posit, _income):  
        self.name = name  
        self.surn = surname
        self.pos = posit
        self.inc = _income
        
class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surn}')

    def get_total_income(self):
        print(f'Доход сотрудника - {int(self.inc["wage"]) + int(self.inc["bonus"])}')

incm = {}
name = input('Введите имя сотрудника: ')
surname = input('Введите Фамилию сотрудника: ')
posit = input('Введите должность сотрудника: ')
incm['wage'] = input('Введите оклад сотрудника: ')
incm['bonus'] = input('Введите премию сотрудника: ')

clss1 = Position(name, surname, posit, incm)
clss1.get_full_name()
clss1.get_total_income()
