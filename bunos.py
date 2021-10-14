data_list = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
new_list = []

while data_list:
    minimum = data_list[0]  
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)
