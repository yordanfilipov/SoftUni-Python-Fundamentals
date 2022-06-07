def swap_numbers(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]
    return arr


def multiply_numbers(arr, first, second):
    arr[first] = arr[first] * arr[second]
    return arr


def decrease_numbers(arr):
    arr = [(el-1) for el in arr]
    return arr


array = [int(el) for el in input().split()]

command = input()

while not command == "end":
    command = command.split()
    action = command[0]
    if len(command) > 1:
        first_index, second_index = command[1], command[2]
        first_index = int(first_index)
        second_index = int(second_index)
    if action == "swap":
        array = swap_numbers(array, first_index, second_index)
    elif action == "multiply":
        array = multiply_numbers(array, first_index, second_index)
    elif action == "decrease":
        array = decrease_numbers(array)

    command = input()
print(*array, sep=", ")