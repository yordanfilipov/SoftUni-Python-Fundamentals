text = input()
result = ""
command = input()

while not command == "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        result = ""
        for i in range(len(text)):
            if i % 2 == 1:
                result += text[i]
        text = result
        print(text)
    elif action == "Cut":
        ind, length = command[1:]
        ind = int(ind)
        length = int(length)
        substring = text[ind:(ind + length)]
        if substring in text:
            text = text.replace(substring, "", 1)
        print(text)
    elif action == "Substitute":
        substring, substitute = command[1:]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {text}")
