class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        nom = int(input('Type the nominator: '))
        denom = int(input('Type the denominator: '))
        if denom == 0:
            raise OwnError('Error! Division by zero!')
    except ValueError:
        print('Wrong number!')
    except OwnError as err:
        print(err)
    else:
        print(f'{round(nom/denom, 2)}')
        break
