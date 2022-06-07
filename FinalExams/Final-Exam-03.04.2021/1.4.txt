def reverse_string(substring):
    result = ""
    for i in range(len(substring) - 1, -1, -1):
        result += substring[i]
    return result


username = input()

command = input()
while not command == "Sign up":
    command = command.split()
    action = command[0]
    if action == "Case":
        if command[1] == "lower":
            username = username.lower()
        elif command[1] == "upper":
            username = username.upper()
        print(username)
    elif action == "Reverse":
        start_index, end_index = command[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            print(reverse_string(substring))
    elif action == "Cut":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif action == "Replace":
        char = command[1]
        if char in username:
            username = username.replace(char, "*")
            print(username)
    elif action == "Check":
        char = command[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    command = input()
