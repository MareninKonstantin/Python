start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
stop_list = [i for i in start_list if start_list.count(i) == 1]

print(stop_list)
