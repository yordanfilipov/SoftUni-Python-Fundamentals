targets = [int(el) for el in input().split()]
command = input()
count = 0

while not command == "End":
    index = int(command)
    if 0 <= index < len(targets):
        if not targets[index] == -1: #TO CHECK
            count += 1
            current_value = int(targets[index])
            targets[index] = -1
            for index in range(len(targets)):
                if not targets[index] == -1:
                    if targets[index] > current_value:
                        targets[index] -= current_value
                    else:
                        targets[index] += current_value
    command = input()
targets = [str(el) for el in targets]
targets_unpacked = ' '.join(targets)
print(f"Shot targets: {count} -> {targets_unpacked}")