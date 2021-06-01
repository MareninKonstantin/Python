with open('test3.txt', 'r',encoding = 'utf-8') as f:
    mid_sal = 0   
    text = f.readlines()
    print('Список сотрудников с зарплатой ниже 20 000:');    
    for line in text:
        surn, salary = line.split()
        mid_sal += int(salary)
        if int(salary) < 20000:
            print(surn);
    print(f'\nСредний доход сотрудника: {mid_sal/len(text)}')
