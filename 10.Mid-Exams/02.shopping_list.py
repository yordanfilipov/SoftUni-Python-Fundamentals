shopping_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    command = command.split()
    action = command[0]
    if action == "Urgent":
        if not command[1] in shopping_list:
            shopping_list.insert(0, command[1])
    elif action == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif action == "Correct":
        if command[1] in shopping_list:
            index = shopping_list.index(command[1])
            shopping_list.remove(command[1])
            shopping_list.insert(index, command[2])
    elif action == "Rearrange":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
    command = input()

print(*shopping_list, sep=", ")