class Matrix:  

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        #-----Задаем ширину матрицы для вывода-----
        matrix_width = 10
        num_in_str = ''        
        for i in self.my_list:
            output_matrix_row = []
            for j in i:
                num_in_str = num_in_str + str(j)
                for k in range(matrix_width - len(str(j))):                   
                    num_in_str = num_in_str + ' '
            num_in_str = num_in_str + '\n'       
        return num_in_str[:len(num_in_str)-1]

    def __add__(self, other):
        temp_matrix_row = []
        cnt_row = len(self.my_list)
        cnt_col = len(self.my_list[0])
        for i in range(cnt_row):
            temp_matrix_col = []
            for j in range(cnt_col):
                temp_matrix_col.append(self.my_list[i][j] + other.my_list[i][j])
            temp_matrix_row.append(temp_matrix_col)
        return Matrix(temp_matrix_row)
        

clss1 = Matrix([[31, 22], [37, 43], [51, 86]])
clss2 = Matrix([[69, 79], [65, 60], [53, 19]])
print(clss1 + clss2)
