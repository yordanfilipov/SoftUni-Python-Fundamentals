input_string = input()
input_list = input_string.split(" ")
opposite_list = []

for i in input_list:
    num = int(i)
    if num > 0:
        opposite_list.append(-num)
    elif num < 0:
        opposite_list.append((-1) * num)
    else:
        opposite_list.append(0)
print(opposite_list)