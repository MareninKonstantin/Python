with open('test4.txt', 'r+',encoding = 'utf-8') as f1:
    numbers = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}
    my_list = []
    while True:
        line = f1.readline()
        if not line:
            break
        else:
            num = line.split()
            num.insert(0,numbers.get(num[0]))
            num.pop(1)
            string = ' '.join(num)
            my_list.append(string + '\n')
    print(my_list)
    
with open('new4.txt', 'w',encoding = 'utf-8') as f1:
    f1.writelines(my_list)
