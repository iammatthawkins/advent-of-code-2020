import csv

def get_row_col(the_list, min, max):
    the_range = max - min
    for char in the_list:
        if char in ['F','L']:
            max -= the_range//2 + 1
        elif char in ['B', 'R']:
            min += the_range//2 + 1
        the_range = max - min
    return min 

with open('input.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    seats = [row[0] for row in reader]

ROWS = 127  # 0 -> 127  = 128 total
COLS = 7    # 0 -> 8    = 8 total

highest_total = 0

for seat in seats:
    row = get_row_col(seat[:7], 0, ROWS)
    col = get_row_col(seat[7:], 0, COLS)
    if (row * 8) + col > highest_total:
        highest_total = (row * 8) + col

print(highest_total)