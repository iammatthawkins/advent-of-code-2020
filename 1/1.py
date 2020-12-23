
with open('input.csv') as file:
    int_list = [int(i) for i in file.read().splitlines()]
    
for ele in int_list:
    popped_ele = int_list.pop()

    for value in int_list:
        if popped_ele + value == 2020:
            print(f'{popped_ele} + {value} = 2020')
            print(f'{popped_ele} x {value} = {popped_ele * value}')
