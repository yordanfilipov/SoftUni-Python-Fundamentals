# strings = [int(el) for el in input().split()]
strings = input().split()
command = input()

while not command == "end":
    command = command.split()
    action = command[0]
    if action == "reverse":
        first_index = int(command[2])
        second_index = first_index + (int(command[4]) - 1)
        first_part = strings[:first_index]
        second_part = strings[second_index + 1:]
        middle_part = strings[first_index:second_index + 1]
        middle_part.reverse()
        strings = first_part + middle_part + second_part
    elif action == "sort":
        first_index = int(command[2])
        second_index = first_index + (int(command[4]) - 1)
        first_part = strings[:first_index]
        second_part = strings[second_index + 1:]
        middle_part = strings[first_index:second_index + 1]
        middle_part.sort()
        strings = first_part + middle_part + second_part
    elif action == "remove":
        remove_count = int(command[1])
        for i in range(remove_count):
            strings.pop(0)
    command = input()

print(*strings, sep=", ")