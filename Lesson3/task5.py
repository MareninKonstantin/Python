def sum_func():
    summ = 0
    fl = False
    while True:
        string1 = input('Введите последовательность чисел, разделенную пробелами: ')
        my_list = string1.split()
        for i in my_list:
            if i == '*':
                fl = True
                break
            else:
                try:
                    summ += int(i)
                except ValueError:
                    print(i + ' - не число!')
        print(my_list)
        print(summ)
        if fl:
            break

sum_func()
