notes = [0] * 100
command = input()

while not command == "End":
    tokens = command.split('-')
    priority = int(tokens[0])
    note = tokens[1]
    notes.insert(priority, note)

    command = input()
result = []
for el in notes:
    if not el == 0:
        result.append(el)
print(result)