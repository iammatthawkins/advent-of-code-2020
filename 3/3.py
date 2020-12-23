import csv

with open('input.txt','r') as csvfile:
    reader = csv.reader(csvfile)
    old_list = [row for row in reader]

routes = [list(lst[0]) for lst in old_list]

#Attributes of list
ROUTE_HEIGHT = len(routes)
ROUTE_LEN = len(routes[0])

#trackers for the loop
current_col = 0
total_trees = 0

for i in range(ROUTE_HEIGHT - 1):
    current_col = (current_col + 3) - ROUTE_LEN  if current_col + 3 >= ROUTE_LEN else current_col + 3
    if routes[i + 1][current_col] == '#':
        total_trees += 1

print(total_trees)
