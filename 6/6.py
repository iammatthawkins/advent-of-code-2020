import csv

#inport the input file as a list.
with open('input.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    old_list = [row for row in reader]

#find length of list
list_len = len(old_list)

#create empty list to hold cleansed input file
new_list = []
temp_str = ''
total = 0

# loop through the list
# am condensing each passport into one line only
for i in range(list_len):
    if old_list[i] != []:
        temp_str += old_list[i][0]
    
    if i == list_len - 1 or old_list[i] == []:
        new_list.append(set(temp_str))
        temp_str = ''

for answers in new_list:
    total += len(answers)

print(total)