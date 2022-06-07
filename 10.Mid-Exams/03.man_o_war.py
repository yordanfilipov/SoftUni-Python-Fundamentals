def fire(i, d, warship):
    if 0 <= i < len(warship):
        warship[i] -= d
        if war_ship[i] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return warship


def defend(start, end, dmg, pirate):
    if 0 <= start < len(pirate) and 0 <= end < len(pirate):
        for ind in range(start, end + 1):
            pirate[ind] -= dmg
            if pirate[ind] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return pirate


def repair(i, hlt, pirate):
    if 0 <= i < len(pirate):
        pirate[i] += hlt
        if pirate[i] > max_health:
            pirate[i] = max_health
    return pirate


pirate_ship = [int(el) for el in input().split('>')]
war_ship = [int(el) for el in input().split('>')]
max_health = int(input())
lower_status = max_health * 0.2
lower_sections = []

command = input()

while not command == "Retire":
    command = command.split()
    action = command[0]
    if action == "Fire":
        index, damage = command[1], command[2]
        index = int(index)
        damage = int(damage)
        war_ship = fire(index, damage, war_ship)
    elif action == "Defend":
        start_index, end_index, damage = command[1], command[2], command[3]
        start_index = int(start_index)
        end_index = int(end_index)
        damage = int(damage)
        pirate_ship = defend(start_index, end_index, damage, pirate_ship)
    elif action == "Repair":
        index, health = command[1], command[2]
        index = int(index)
        health = int(health)
        pirate_ship = repair(index, health, pirate_ship)
    elif action == "Status":
        lower_sections = [el for el in pirate_ship if el < lower_status]
        count = len(lower_sections)
        print(f"{count} sections need repair.")
    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ship)}")