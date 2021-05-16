num = int(input('Введите целое положительное число: '))
num_res = num
max_num = 0
while num_res > 0:
    if max_num < num_res % 10:
        max_num = num_res % 10 
    num_res = num_res // 10
print(max_num)
