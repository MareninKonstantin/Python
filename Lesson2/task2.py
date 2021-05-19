list = []
while True:
    el = input('Введите новый элемент списка (чтобы завершить ввод - введите stop): ')
    if el.lower() == 'stop':
        break
    else:
        list.append(el)

for el in range(len(list) // 2):
    tmp = list[el*2+1]
    list[el*2+1] = list[el*2]
    list[el*2] = tmp

print(list)
