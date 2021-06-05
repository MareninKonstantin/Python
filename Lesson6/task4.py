class Car:  
    
    def __init__(self, speed, color, name, is_police):  
        self.spd = speed
        self.clr = color
        self.nam = name
        self.plc = is_police

    def info(self):
        if self.plc:
            typ = 'полицейская'
        else:
            typ = 'не полицейская'
        print(f'Авто: {self.nam}; Цвет: {self.clr}; Тип: {typ}; Скорость: {self.spd}') 

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        self.dir = direction
        print(f'Turn to the {self.dir}')

    def show_speed(self):
        print(self.spd)

class TownCar(Car):
    
    def show_speed(self):
        if self.spd > 60:
            print('Превышение по скорости!')
        else:
            print(self.spd)

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.spd > 40:
            print('Превышение по скорости!')
        else:
            print(self.spd)            

class PoliceCar(Car):
    pass

clss1 = TownCar(50, 'green', 'VW', False)
clss2 = SportCar(250, 'black', 'BMW', False)
clss3 = WorkCar(50, 'white', 'Lada', False)
clss4 = PoliceCar(150, 'blue', 'Lamborgini', True)
clss1.info()
clss2.info()
clss3.info()
clss4.info()
clss1.go()
clss1.stop()
clss1.turn('left')
clss1.show_speed()
clss2.show_speed()
clss3.show_speed()
clss4.show_speed()
