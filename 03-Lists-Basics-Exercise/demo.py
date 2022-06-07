command = input().split("#")
whater = int(input())
new_list = []
total_fire = 0
ceill = 0

print("Cells:")

for elements in range(len(command)):
    new_list.append(command[elements].split())
for elements in range(len(new_list)):
    if new_list[elements][0] == 'High' and 81 <= int(new_list[elements][2]) <= 125:
        ceill = int(new_list[elements][2])
    elif new_list[elements][0] == 'Medium' and 51 <= int(new_list[elements][2]) <= 80:
        ceill = int(new_list[elements][2])
    elif new_list[elements][0] == 'Low' and 1 <= int(new_list[elements][2]) <= 50:
        ceill = int(new_list[elements][2])
    else:
        continue
    whater -= ceill
    if whater < 0:
        continue
    print(f' - {ceill}')
    total_fire += ceill
effort = 0.25 * total_fire
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')