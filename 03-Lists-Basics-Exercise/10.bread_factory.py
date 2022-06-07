events = input().split("|")

current_energy = 100
current_coins = 100
gained_energy = 0
bankrupt = False

for event in events:
    command, number = event.split("-")
    number = int(number)

    if command == "rest":
        if current_energy + number > 100:
            gained_energy = 100 - current_energy
            current_energy = 100
        else:
            current_energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif command == "order":
        if current_energy >= 30:
            current_energy -= 30
            current_coins += number
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print(f"You had to rest!")

    else:
        if current_coins > number:
            current_coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            bankrupt = True
            break

if not bankrupt:
    print(f"Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")


