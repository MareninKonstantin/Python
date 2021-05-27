def int_func(text):
    if text.lower() == text:
        print(text.title())
    else:
        print('Не соблюдены условия задачи!')
        int_func(input('Введите строку слов маленькими буквами, разделенную пробелами: '))
        
int_func(input('Введите строку слов маленькими буквами, разделенную пробелами: '))

