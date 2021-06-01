with open('test7.txt','r') as f:
    my_list = f.readlines()

firms_dict = {}
for el in my_list:
#    temp_list = el.split()
    firm, prop, sal, rate = el.split()
    profit = int(sal) - int(rate)
    firms_dict.update({firm : profit})

average_profit = 0    
for el1 in firms_dict:
    if firms_dict.get(el1) > 0:
        average_profit += firms_dict.get(el1)
average_profit = average_profit/len(firms_dict)
av_prof = {'average_profit' : average_profit}
my_list = [firms_dict, av_prof]
print(my_list)

import json

with open("my_file.json", "w") as f:
    json.dump(my_list, f)

#with open("my_file.json") as f:
#    data = json.load(f)
#print(data)
