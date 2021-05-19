string1 = input('Введите строку, разделенную пробелами: ')
list = string1.split()
 
for ind, el in enumerate(list):
    print(ind + 1, el[0:10])
