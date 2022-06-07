targets = [int(target) for target in input().split()]
command = input()
while command != 'End':
    event, index, value = command.split(' ')
    index = int(index)
    value = int(value)
    if event == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            targets = [target for target in targets if target > 0]
    if event == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    if event == 'Strike':
        if 0 <= index < len(targets) and index-value >= 0 and index+value < len(targets):
            if index-value < 0 and index+value > len(targets)-1:
                pass
            else:
                targets = [target for target in targets if target not in targets[index-value:index+value+1]]
        else:
            print('Strike missed!')
    command = input()
print('|'.join([str(target) for target in targets]))