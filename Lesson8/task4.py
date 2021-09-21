class warehouse:
    def __init__(self, number, addr):
        self.num = number
        self.addr = addr

class off_eq:
    def __init__(self, firm, model, price):
        self.firm = firm
        self.model = model
        self.price = price

    def __str__(self):
        return f'Устройство: {self.firm}\nМодель: {self.model}\nЦена: {self.price}\n'

class printer(off_eq):
    def __init__(self, firm, model, price, is_color):
        super().__init__(firm, model, price)
        self.is_color = is_color

    def __str__(self):
        return f'Устройство: {self.firm}\nМодель: {self.model}\nЦена: {self.price}\nЦветная печать: {self.is_color}'
        
class scanner(off_eq):
    def __init__(self, firm, model, price, resolution):
        super().__init__(firm, model, price)
        self.resol = resolution

    def __str__(self):
        return f'Устройство: {self.firm}\nМодель: {self.model}\nЦена: {self.price}\nРазрешение: {self.resol}'
        
class copier(off_eq):
    def __init__(self, firm, model, price, paper_format):
        super().__init__(firm, model, price)
        self.paper_f = paper_format

    def __str__(self):
        return f'Устройство: {self.firm}\nМодель: {self.model}\nЦена: {self.price}\nФормат бумаги: {self.paper_f}'

class1 = printer('HP', 'LaserJet M507', 45000, False)
class2 = scanner('Canon', 'LIDE400', 7000, 4800)
class3 = copier('Xerox', 'WorkCentre B205N', 15000, 'A4')
print(class1, class2, class3, sep = '\n\n')

