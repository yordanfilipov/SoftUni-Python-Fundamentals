initial_loot = input().split('|')
command = input()
stolen_items = []
pirate_credits = 0

while not command == "Yohoho!":
    command = command.split()
    action = command.pop(0)
    if action == "Loot":
        for el in command:
            if el not in initial_loot:
                initial_loot.insert(0, el)
    elif action == "Drop":
        index = int(command[0])
        if 0 <= index < len(initial_loot):
            dropped_element = initial_loot.pop(index)
            initial_loot.append(dropped_element)
    elif action == "Steal":
        stolen_count = int(command[0])
        for stolen in range(stolen_count):
            if not len(initial_loot):
                break
            stolen_items.insert(0, initial_loot.pop())
        print(*stolen_items, sep=', ')
    command = input()
    stolen_items = []

if len(initial_loot) > 0:
    for el in initial_loot:
        pirate_credits += len(el)
    average_treasure = pirate_credits / int(len(initial_loot))
    print(f"Average treasure gain: {average_treasure:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")