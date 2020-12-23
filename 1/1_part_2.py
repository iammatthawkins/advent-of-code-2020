import csv

with open('input.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    mylist = []
    for row in reader:
        new_value = int(row[0])
        mylist.append(new_value)

x, y, z = len(mylist), len(mylist), len(mylist)

finish = False

for first in range(x):
    for second in range(y):
        for third in range(z):
            if mylist[first] + mylist[second] + mylist[third] == 2020:
                print(mylist[first] * mylist[second] * mylist[third])
                finish = True
        if finish == True:
            break
    if finish == True:
        break
        

            

