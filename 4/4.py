import csv

def create_dict(passport_string):
    temp_list = passport_string.split()
    temp_dict = {
        "byr": None,
        "iyr": None,
        "eyr": None,
        "hgt": None,
        "hcl": None,
        "ecl": None,
        "pid": None,
        "cid": None
    }
    for item in temp_list:
        k = item[:3]
        temp_dict[k] = item[4:]
    return temp_dict

#inport the input file as a list.
with open('input.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    old_list = [row for row in reader]

#find length of list
list_len = len(old_list)

#create empty list to hold cleansed input file
new_list = []
temp_str = None

# loop through the list
# am condensing each passport into one line only
for i in range(list_len):
    if old_list[i] == []:
        new_list.append(create_dict(temp_str))
        temp_str = None
    elif temp_str == None:
        temp_str = old_list[i][0]
    else:
        temp_str += ' '
        temp_str += old_list[i][0]
    if i == list_len - 1:
        new_list.append(create_dict(temp_str))

valid_passports = 0

for passport in new_list:
    count_none = 0
    for v in passport.values():
        if v == None:
            count_none += 1
    if count_none == 0:
        valid_passports += 1
    elif count_none == 1 and passport.get('cid') == None:
        valid_passports += 1

print(valid_passports)