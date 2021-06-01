with open('test.txt','w',encoding = 'utf-8') as f:
    while True:
        text = input('Введите строку: ')
        if text == '':
            break
        else:
            f.write(text + '\n')
