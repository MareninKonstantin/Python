class warehouse:
    def __init__(self, number, addr):
        self.num = number
        self.addr = addr
        self.dic_wrh = {}
        self.dic_comp = {}

    def new_eq(self, eq, count):
        self.firm = eq.firm
        self.model = eq.model

        if self.dic_wrh.get(self.firm) is None:
            self.dic_wrh.update({self.firm : {self.model : count}})
        else:
            temp_dict = self.dic_wrh.get(self.firm)
            if temp_dict.get(self.model) is None:
                temp_dict.update({self.model : count})
            else:
                temp_dict.update({self.model : temp_dict.get(self.model) + count})
            self.dic_wrh.update({self.firm : temp_dict})

    def to_company(self, company, eq, count):
        self.comp = company
        self.firm = eq.firm
        self.model = eq.model
        temp_dic = self.dic_wrh.get(self.firm)

        print(temp_dic.get(self.model), count)

        if temp_dic.get(self.model) >= count:
            temp_dic.update({self.model : temp_dic.get(self.model) - count})
            self.dic_wrh.update({self.firm : temp_dic})
            if self.dic_comp.get(self.comp) is None:
                self.dic_comp.update({self.comp : {self.firm : {self.model : count}}})
            else:
                temp_dict1 = self.dic_comp.get(self.comp)
                if temp_dict1.get(self.firm) is None:
                    temp_dict1.update({self.firm : {self.model : count}})
                    self.dic_comp.update({self.firm : temp_dict1})
                else:
                    temp_dict2 = self.temp_dict1.get(self.firm)
                    if temp_dict2.get(self.model) is None:
                        temp_dict2.update({self.model : count})
                    else:
                        temp_dict2.update({self.model : temp_dict1.get(self.model) + count})
                    self.temp_dict1.update({self.firm : temp_dict2})
                    self.dic_comp.update({self.firm : temp_dict1})                    
        else:
            print('Недостаточно товара на складе!')
        
    def __str__(self):
        return f'Склад: {self.num}\nНа складе: {self.dic_wrh}\nПередано со склада: {self.dic_comp}'

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

eq_printer = printer('HP', 'LaserJet M507', 45000, False)
eq_scanner = scanner('Canon', 'LIDE400', 7000, 4800)
eq_copier = copier('Xerox', 'WorkCentre B205N', 15000, 'A4')

class1 = warehouse('#1', 'Kirov')
class1.new_eq(eq_printer, 10)
class1.new_eq(eq_scanner, 10)
class1.new_eq(eq_copier, 10)
class1.new_eq(eq_printer, 10)
print(class1)

class1.to_company('Sberbank', eq_printer, 1)
print(class1)

class1.new_eq(eq_scanner, 5)
class1.to_company('VTB', eq_printer, 2)
print(class1)
