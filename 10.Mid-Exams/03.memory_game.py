def out_of_index(first, second, elements):
    if first < 0 or first >= len(elements):
        return True
    if second < 0 or second >= len(elements):
        return True
    if first == second:
        return True
    return False


elements = input().split()
command = input()
moves = 0

while not command == "end":
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    moves += 1
    first_index = int(command.split()[0])
    second_index = int(command.split()[1])
    if out_of_index(first_index, second_index, elements):
        position = len(elements) // 2
        elements.insert(position, f"-{moves}a")
        elements.insert(position + 1, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue
    if elements[first_index] == elements[second_index]:
        matching_element = elements[first_index]
        # elements = [el for el in elements if not el == matching_element]
        elements.remove(matching_element)
        elements.remove(matching_element)
        print(f"Congrats! You have found matching elements - {matching_element}!")
        command = input()
        continue
    if elements[first_index] != elements[second_index]:
        print("Try again!")
    command = input()

if command == "end":
    print("Sorry you lose :(")
    print(*elements, sep=" ")