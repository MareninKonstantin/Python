class Complex_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 0:
            return f'{self.a}'
        elif self.b == 1:
            return f'{self.a} + i'
        elif self.b == -1:
            return f'{self.a} - i'          
        elif self.b > 0:
            return f'{self.a} + {self.b}*i'              
        else:
            return f'{self.a} - {abs(self.b)}*i'

    def __add__(self, other):
        return Complex_number(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex_number(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

while True:
    try:
        ex1 = Complex_number(int(input('Введите А1: ')), int(input('Введите B1: ')))
        ex2 = Complex_number(int(input('Введите А2: ')), int(input('Введите B2: ')))
    except ValueError:
        print('Введено не корректное число! Повторите ввод!')
    else:
        print(f'Результат сложения: {ex1 + ex2}')
        print(f'Результат умножения: {ex1 * ex2}')
        break     
