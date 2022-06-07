def check_if_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


targets = [int(el) for el in input().split()]

command_data = input()

while not command_data == "End":
    command, index, val = command_data.split()
    index = int(index)
    val = int(val)
    if command == "Shoot":
        if check_if_index_is_valid(index, len(targets)):
            targets[index] -= val
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if check_if_index_is_valid(index, len(targets)):
            targets.insert(index, val)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        left_most_index = index - val
        right_most_index = index + val
        if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(
                targets)) and check_if_index_is_valid(right_most_index, len(targets)):
            left_unstriked_part = targets[:left_most_index]
            right_unstriked_part = targets[right_most_index + 1:]
            targets = left_unstriked_part + right_unstriked_part
        else:
            print("Strike missed!")

    command_data = input()

print('|'.join([str(el) for el in targets]))