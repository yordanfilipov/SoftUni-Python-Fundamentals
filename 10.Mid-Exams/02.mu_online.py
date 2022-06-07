rooms = [el for el in input().split("|")]

MAX_HEALTH = 100
bitcoins = 0
health = 100
amount = 0
current_health = 0

for room in range(len(rooms)):
    command, value = rooms[room].split()
    value = int(value)
    if command == "potion":
        current_health = health
        health += value
        amount = value
        if health > MAX_HEALTH:
            amount = MAX_HEALTH - current_health
            health = MAX_HEALTH
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room + 1}")
            exit()
print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")