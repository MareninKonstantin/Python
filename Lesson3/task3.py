def my_func(*args):
    my_list = []
    try:
        for i in args:
            num = int(i)
            my_list.append(num)
#        my_list = list(args)
        my_list.sort(reverse = True)       
        print("Сумма двух наибольших чисел равна " + str(my_list[0]+my_list[1]))
    except ValueError:
        print('Вы ввели не число!')
        my_func(input('Введите 1ое число: '),input('Введите 2ое число: '),input('Введите 3ое число: '))

my_func(input('Введите 1ое число: '),input('Введите 2ое число: '),input('Введите 3ое число: '))
