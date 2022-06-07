moving_targets = input().split()

command = input()

while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if action == "Shoot" and 0 <= index < len(moving_targets):
        current_index = int(moving_targets[index])
        current_index -= value
        if current_index <= 0:
            moving_targets.pop(index)
        else:
            moving_targets[index] = str(current_index)
    elif action == "Add":
        if index >= len(moving_targets):
            print("Invalid placement!")
        else:
            moving_targets.insert(index, str(value))
    elif action == "Strike":
        start_index = index - value
        stop_index = index + value
        if start_index >= 0 and stop_index < len(moving_targets):
            del moving_targets[start_index:stop_index + 1]
        else:
            print("Strike missed!")
    command = input()
print("|".join(moving_targets))

