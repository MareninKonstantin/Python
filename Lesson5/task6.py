with open('test6.txt','r') as f:
    my_list = f.readlines()

my_dict = {}
for el in my_list:
    temp_list = el.split()
    summary = 0    
    for i in temp_list:
        str_num = ''
        for j in i:
            if ord(j) >=48 and ord(j) <58:
                str_num = str_num + j
        if str_num != '':
            summary = summary + int(str_num)
    my_dict.update({temp_list[0][:len(temp_list[0])-1] : summary})

print(my_dict)
