import csv

with open('input.txt','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    old_list = [row for row in reader]

#Each element in list is a list of 3 elements. Need to alter
# element 0: need to split into 2 ints - min and max
# element 1: need to remove trailing colon
# element 2: can use as is

#List will then become a series of tuples:
# ele 0: min number of times
# ele 1: max number of times
# ele 2: char to exist between min and max times
# ele 3: password to search for char

new_list = []

for ele in old_list:
    ele0_list = ele[0].split("-")
    ele0 = int(ele0_list[0])
    ele1 = int(ele0_list[1])
    ele2 = ele[1][0]
    ele3 = ele[2]
    new_list.append((ele0, ele1, ele2, ele3))

count_correct = 0

for ele in new_list:
    counter = ele[3].count(ele[2]) 
    #print(counter)
    if counter >= ele[0] and counter <= ele[1]:
        count_correct += 1

print(count_correct)