class Road:  
    wght = 25
    thick = 0.05
    
    def __init__(self, _length, _width):  
        self.l = _length  
        self.w = _width   
        
    def estimation(self):  
        return self.l * self.w * self.wght * self.thick

clss1 = Road(20, 5000)  
clss2 = Road(20, 1000)  
print(f' Масса дорожного полотна - {clss1.estimation()} кг')
print(f' Масса дорожного полотна - {clss2.estimation()} кг')
