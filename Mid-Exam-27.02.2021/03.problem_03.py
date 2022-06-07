cards = input().split(':')
command = input()

deck = []

while not command == "Ready":
    command = command.split()
    action = command[0]
    if action == "Add":
        card = command[1]
        if card not in cards:
            print("Card not found.")
        else:
            deck.append(card)
    elif action == "Insert":
        card = command[1]
        index = int(command[2])
        if card not in cards or index < 0 or index >= len(deck):
            print("Error!")
        else:
            deck.insert(index, card)
    elif action == "Remove":
        card = command[1]
        if card not in deck:
            print("Card not found.")
        else:
            deck.remove(card)
    elif action == "Swap":
        card_1 = command[1]
        card_2 = command[2]
        index_1 = deck.index(card_1)
        index_2 = deck.index(card_2)
        deck[index_1], deck[index_2] = deck[index_2], deck[index_1]
    elif action == "Shuffle":
        deck.reverse()
    command = input()

print(*deck, sep=" ")