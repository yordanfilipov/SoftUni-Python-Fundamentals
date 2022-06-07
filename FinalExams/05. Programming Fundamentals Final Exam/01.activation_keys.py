raw_key = input()

line = input()
while not line == "Generate":
    line = line.split(">>>")
    action = line[0]
    if action == "Contains":
        substring = line[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        case, start, end = line[1:]
        start = int(start)
        end = int(end)
        if case == "Upper":
            raw_key = raw_key[:start] + raw_key[start:end].upper() + raw_key[end:]
        elif case == "Lower":
            raw_key = raw_key[:start] + raw_key[start:end].lower() + raw_key[end:]
        print(raw_key)
    elif action == "Slice":
        start, end = line[1:]
        start = int(start)
        end = int(end)
        raw_key = raw_key[:start] + raw_key[end:]
        print(raw_key)
    line = input()

print(f"Your activation key is: {raw_key}")