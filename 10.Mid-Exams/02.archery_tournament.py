targets = list(map(int, input().split("|")))

command = input()
points = 0

while not command == "Game over":
    data = command.split()
    type_command = data[0]
    if type_command == "Shoot":
        direction, starting_index, length = data[1].split('@')
        starting_index = int(starting_index)
        length = int(length)
        if starting_index in range(len(targets)):
            if direction == "Left":
                index = (starting_index - length) % len(targets)
            else:
                index = (starting_index + length) % len(targets)
            if targets[index] < 5:
                points += targets[index]
                targets[index] = 0
            else:
                points += 5
                targets[index] -= 5
    elif type_command == "Reverse":
        targets = targets[::-1]
    command = input()

print(' - '.join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")