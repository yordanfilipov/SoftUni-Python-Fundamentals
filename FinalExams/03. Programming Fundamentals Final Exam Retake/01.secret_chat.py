def reverse_string(substring):
    result = ""
    for i in range(len(substring) - 1, -1, -1):
        result += substring[i]
    return result


text = input()
command = input()

while not command == "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        index = int(command[1])
        text = text[:index] + " " + text[index:]
        print(text)
    elif action == "Reverse":
        substring = command[1]
        if substring in text:
            reversed_substring = reverse_string(substring)
            text = text.replace(substring, "", 1)
            text = text + reversed_substring
            print(text)
        else:
            print("error")
    elif action == "ChangeAll":
        substring, replacement = command[1:]
        if substring in text:
            text = text.replace(substring, replacement)
            print(text)
    command = input()
print(f"You have a new text message: {text}")