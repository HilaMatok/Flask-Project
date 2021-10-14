import numpy as np


names = open("names.txt", "r")
content = names.readlines()
names.close()

name_split=np.array_split(content, 6)
for idx, array in enumerate(name_split):
    f= open("list{}.txt".format(idx+1), "w+")
    print ("list{}created".format(idx+1))
    for name in array:
        f.write(name)
    f.close()

print ("6 equal lists created, Done!")
