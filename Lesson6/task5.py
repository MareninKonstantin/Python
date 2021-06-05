class Stationery:  
    
    def __init__(self, title):  
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой!')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом!')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером!')
        
clss = Stationery('Фломастер')
clss1 = Pen('Ручка')
clss2 = Pencil('Карандаш')
clss3 = Handle('Маркер')
clss.draw()
clss1.draw()
clss2.draw()
clss3.draw()
