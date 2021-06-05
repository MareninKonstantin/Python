class TrafficLight:
    __color = 'Red'
    def running(self, clr):
        from time import sleep
        self._TrafficLight__color = clr
        print(clr)
        if clr == 'Red':
            sleep(7)
        else:
            if clr == 'Yellow':
                sleep(2)
            else:
                sleep(5)
        
clss = TrafficLight()
clss.running('Red')
clss.running('Yellow')
clss.running('Green')
