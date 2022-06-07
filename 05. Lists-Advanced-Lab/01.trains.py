trains = int(input())

trains_list = [0] * trains

command = input()

while not command == "End":
    tokens = command.split()
    if tokens[0] == "add":
        trains_list[-1] += int(tokens[1])
    elif tokens[0] == "insert":
        trains_list[int(tokens[1])] += int(tokens[2])
    elif tokens[0] == "leave":
        trains_list[int(tokens[1])] -= int(tokens[2])
    command = input()

print(trains_list)