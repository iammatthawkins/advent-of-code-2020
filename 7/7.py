import csv

with open('input1.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ')
    old_list = [row for row in reader]

    print(old_list)

for sentence in old_list:


"""
{
     'bag colour': [(bag: n), {bag, n)]
    ,'bag colour': [(bag: n), {bag, n)]
}
"""
