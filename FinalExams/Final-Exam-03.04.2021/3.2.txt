command = input()

usernames = {}

while not command == "Log out":
    command = command.split(": ")
    action = command[0]
    if action == "New follower":
        username = command[1]
        if username not in usernames:
            usernames[username] = 0
    elif action == "Like":
        username, count = command[1:]
        count = int(count)
        if username not in usernames:
            usernames[username] = count
        else:
            usernames[username] += count
    elif action == "Comment":
        username = command[1]
        if username not in usernames:
            usernames[username] = 1
        else:
            usernames[username] += 1
    elif action == "Blocked":
        username = command[1]
        if username in usernames:
            del usernames[username]
        else:
            print(f"{username} doesn't exist.")
    command = input()

sorted_usernames = sorted(usernames.items(), key=lambda x: (-x[1], x[0]))

print(f"{len(usernames)} followers")

for user, points in sorted_usernames:
    print(f"{user}: {points}")