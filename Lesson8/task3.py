class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        
err = 'error'
mylist = []
while True:
    el = input('Type the number (to stop - type "stop"): ')
    if el.lower() == 'stop':
        break
    else:
        try:
            if el.isdigit():
                el = int(el)
            else:
                raise OwnError('Wrong number!')
        except OwnError as err:
            print(err)
        else:
            mylist.append(el)

print(mylist)
