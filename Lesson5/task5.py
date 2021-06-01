try:
    try:
        with open('test5.txt','w+',encoding = 'utf-8') as f:
            f.write(input('Введите набор чисел, разделенных пробелами: '))
            f.seek(0)
            my_list = f.read().split()
            num = 0
            for el in my_list:
                num += int(el)
        print(f'Сумма чисел в строке равна {num}')        
    except ValueError:
        print('Введены не корректные числа!')
except IOError:
        print("Произошла ошибка ввода-вывода!")
