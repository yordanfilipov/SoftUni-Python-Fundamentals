energy = int(input())

command = input()
count = 0

while not command == "End of battle":
    enemy_distance = int(command)
    if energy >= enemy_distance:
        energy -= enemy_distance
        count += 1
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        exit()
    if count % 3 == 0:
        energy += count
    command = input()
print(f"Won battles: {count}. Energy left: {energy}")