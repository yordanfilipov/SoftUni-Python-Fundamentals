pirate_ship = list(map(int, input().split(">")))
war_ships = list(map(int, input().split(">")))
max_health_per_section = int(input())

command = input()

while not command == "Retire":
    command_type = command.split()[0]

    if command_type == "Fire":
        index = int(command.split()[1])
        damage = int(command.split()[2])
        if index in range(len(war_ships)):
            war_ships[index] -= damage
            if war_ships[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)
    elif command_type == "Defend":
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])
        damage = int(command.split()[3])
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit(0)
    elif command_type == "Repair":
        index = int(command.split()[1])
        health = int(command.split()[2])
        if index in range(len(pirate_ship)):
            if pirate_ship[index] + health <= max_health_per_section:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = max_health_per_section
    elif command_type == "Status":
        to_repair = sum(map(lambda x: x < max_health_per_section * 0.2, pirate_ship))
        print(f"{to_repair} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ships)}")