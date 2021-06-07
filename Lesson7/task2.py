from abc import ABC, abstractmethod

class clothes_abstract(ABC):  
    
    @abstractmethod
    def __init__(self, param):
        self.param = float(param)

    def __add__(self, other):
        return round(self.param + other.param, 2)
    
    def __str__(self):
        return f'{round(self.param, 2)}'   

class coat(clothes_abstract):

    def __init__(self, param):
        self.param = float(param)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 40:
            print('Слишком маленький размер пальто! Расчет будет произведен по минимальному размеру - 40!')
            self.__param = 40 / 6.5 + 0.5
        elif param > 50:
            print('Слишком большой размер пальто! Расчет будет произведен по максимальному размеру - 50!')
            self.__param = 50 / 6.5 + 0.5
        else:
            self.__param = param / 6.5 + 0.5
        
class suit(clothes_abstract):

    def __init__(self, param):
        self.param = float(param)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 1.5:
            print('Слишком маленький размер костюма! Расчет будет произведен по минимальному размеру - 1.5!')
            self.__param = 1.5 * 2 + 0.3
        elif param > 2.2:
            print('Слишком большой размер костюма! Расчет будет произведен по максимальному размеру - 2.2')
            self.__param = 2.2 * 2 + 0.3
        else:
            self.__param = param * 2 + 0.3

clss1 = coat(input('Введите размер пальто: '))
clss2 = suit(input('Введите высоту костюма: '))
print(f'Расход на первую вещь: {clss1} ед.')
print(f'Расход на вторую вещь: {clss2} ед.')
print(f'Общий расход ткани: {clss1 + clss2} ед.')
