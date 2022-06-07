text = input()
line = input()

while not line == "Decode":
    line = line.split("|")
    action = line[0]
    if action == "Move":
        chars = ""
        count_of_chars = int(line[1])
        for i in range(count_of_chars):
            chars += text[i]
        text = text + chars
        text = text[count_of_chars:]
    elif action == "Insert":
        position, letters = line[1], line[2]
        position = int(position)
        first_half = text[:position]
        second_half = text[position:]
        text = first_half + letters + second_half
    elif action == "ChangeAll":
        old_letter, new_letter = line[1], line[2]
        text = text.replace(old_letter, new_letter)
    line = input()

print(f"The decrypted message is: {text}")