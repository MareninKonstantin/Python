from sys import argv
from itertools import count

try:
    start, finish = map(int,argv[1:])
    if start > finish:
        print('Задано не корректное условие для выхода из цикла!')
    else:
        for el in count(start):
            if el > finish:
                break
            else:
                print(el)
except ValueError:
    print('Вы ввели не целое число!')
