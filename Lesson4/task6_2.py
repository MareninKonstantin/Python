from sys import argv
from itertools import cycle

my_list = [1, 2, 3, 4, 5]

try:
    finish = int(argv[1])
    c = 0
    if finish <=0:
        print('Введено некорректное число!')
    else:
        for el in cycle(my_list):
            if c >= finish:
                break
            print(el)
            c += 1
except ValueError:
    print('Вы ввели не целое число!')
