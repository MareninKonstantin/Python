first_d = float(input('Укажите результат спортсмена в 1ый день пробежки (а):'))
lim_d = float(input('Укажите цель спортсмена (b):'))

day = 1
while first_d < lim_d:
    first_d = first_d * 1.1
    day += 1
print('На '+str(day)
      +'-й день спортсмен достиг результата - не менее '+str(lim_d)+' км')
