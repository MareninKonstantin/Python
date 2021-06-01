with open('test2.txt','r',encoding = 'utf-8') as f:

    text = f.readlines()
    print(f'Количество строк в файле - {len(text)}\n')
    for ind,el in enumerate(text):
        list_w = el.split()
        print(f'Количество слов в {ind + 1} строке - {len(list_w)}')
