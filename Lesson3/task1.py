def division(arg1, arg2):
    try:
        print(float(arg1) / float(arg2))
    except ValueError:
        print('Как минимум один из аргументов не число!')
        division(input('Введите делимое: '),input('Введите делитель: '))
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        division(input('Введите делимое: '),input('Введите делитель: '))

division(input('Введите делимое: '),input('Введите делитель: '))
