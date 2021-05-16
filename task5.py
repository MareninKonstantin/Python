proc = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))

if proc > costs:
    print('Компания отработала с прибылью',round(proc * 100 / costs),'%')
    num_em = int(input('Введите численность сотрудников: '))
    print('Прибыль компании на одного сотрудника',toFixed((proc-costs)/num_em, 2))
elif proc < costs:
    print('Компания отработала с убытком')
else:
    print('Компания отработала в 0')
