class Cell:  

    def __init__(self, cell_amount):
        self.cell_cnt = cell_amount

    def __str__(self):
        return f'{self.cell_cnt}'

    def __add__(self, other):
        return Cell(self.cell_cnt + other.cell_cnt)

    def __sub__(self, other):
        if self.cell_cnt > other.cell_cnt:
            return self.cell_cnt - other.cell_cnt
        else:
            return f'ОШИБКА!\n---Количество ячеек во второй клетке превышает количество ячеек в первой!---'

    def __mul__(self, other):
        return Cell(self.cell_cnt * other.cell_cnt)

    def __truediv__(self, other):
        return Cell(self.cell_cnt // other.cell_cnt)
    
    def make_order(self, col):
        self.mtrx_width = col
        row = self.cell_cnt // self.mtrx_width
        string = '*' * col
        print(f'\nОрганизованная клетка по {col} ячеек в ряду:')
        for i in range(row):
            print(string)
        if self.cell_cnt % self.mtrx_width > 0:
            add_str = '*' * (self.cell_cnt % self.mtrx_width)            
            print(add_str)
'''
        num_in_str = ''        
        for i in self.my_list:
            output_matrix_row = []
            for j in i:
                num_in_str = num_in_str + str(j)
                for k in range(matrix_width - len(str(j))):                   
                    num_in_str = num_in_str + ' '
            num_in_str = num_in_str + '\n'       
        return num_in_str[:len(num_in_str)-1]    '''    

clss1 = Cell(30)
clss2 = Cell(20)
print(f'Количество ячеек после сложения: {clss1 + clss2}')
print(f'Количество ячеек после вычитания: {clss1 - clss2}')
print(f'Количество ячеек после умножения: {clss1 * clss2}')
print(f'Количество ячеек после деления: {clss1 / clss2}')
clss1.make_order(7)
