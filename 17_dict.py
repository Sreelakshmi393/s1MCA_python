dict_unsort = {'apple' : 50, 'orange' : 40, 'grapes' : 35, 'strawberry' : 80}

sorted_dict_asc =  dict(sorted(dict_unsort.items()))
print("Sorted dictionary in ascending order is : ")
for key, value in sorted_dict_asc.items():
    print(f'{key}: {value}')

sorted_dict_des = dict(sorted(dict_unsort.items(),  reverse=True))
print("Sorted dictionary in descnding order is : ")
for key, value in sorted_dict_des.items():
    print(f'{key}:{value}')
