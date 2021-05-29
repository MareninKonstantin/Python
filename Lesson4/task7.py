def fact(n):
    sum = 1
    for el in range(1,int(n)+1):
        sum = sum * el
        yield sum

while True:
    try:
        n = int(input('Введите число для расчета факториала: '))
        for el in fact(n):
            print(el)
        break  
    except ValueError:
        print('Введено не корректное число!')
