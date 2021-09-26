from sys import argv

def salary(time, rate, bonus):
    print('Зарплата сотрудника - ' + str(time * rate + bonus))

time, rate, bonus = map(int, argv[1:])
salary(time, rate, bonus)
