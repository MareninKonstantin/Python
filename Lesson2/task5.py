my_list = [7, 5, 3, 3, 2]
 
while True:
    try:
        new_el = input('Введите новый элемент (для выхода введите "stop"): ')
        if new_el.lower() == 'stop':
            break
        else:
            new_el = int(new_el)
    except ValueError:
        print('Введено не число! Попробуйте заново!')
    else:
        fl = False
        for ind,el in enumerate(my_list):
            if new_el > el:
                fl = True
                my_list.insert(ind,new_el)
                break
        if not fl:
            my_list.append(new_el)
        print(my_list)
