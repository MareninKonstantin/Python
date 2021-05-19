list = ['зима','весна','лето','осень']
#dic = {1:'зима',2:'зима',12:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень'}
dic = {'зима':[1,2,12],'весна':[3,4,5],'лето':[6,7,8],'осень':[9,10,11]}
while True:
    try:
        month = int(input('Введите номер месяца: '))
        if 1 <= month <= 12:
            if month == 12:
                season = 0
            else:   
                season = month // 3
            break   
        else:
            print('Введено некорректное число!')
    except ValueError:
        print('Введено не число!')
 
print('На улице '+str(list[season]+' (через список)'))
for el in dic:
    for el1 in range(3):
        if month == dic[el][el1]:
#            print(el)
            print('На улице '+el+' (через словарь)')
            break
