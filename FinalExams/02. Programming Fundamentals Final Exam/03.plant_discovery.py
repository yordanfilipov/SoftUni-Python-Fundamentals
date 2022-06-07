n = int(input())

plants = {}

for _ in range(n):
    data = input()
    data = data.split("<->")
    plant, rarity = data[:]
    rarity = int(rarity)
    plants[plant] = {'rarity': rarity, 'rating': []}

command = input()
while not command == "Exhibition":
    command = command.split(": ")
    action = command[0]
    if action == "Rate":
        plant_and_rating = command[1].split(" - ")
        plant, rating = plant_and_rating[:]
        rating = int(rating)
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant_and_rating = command[1].split(" - ")
        plant, rarity = plant_and_rating[:]
        rarity = int(rarity)
        if plant in plants:
            plants[plant]['rarity'] = rarity
        else:
            print("error")
    elif action == "Reset":
        plant = command[1]
        if plant in plants:
            plants[plant]['rating'].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()

for plant, data in plants.items():
    if data['rating']:
        avg = sum(data['rating']) / len(data['rating'])
    else:
        avg = 0
    plants[plant]['avg'] = avg

sorted_plants = sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['avg']))

print(f"Plants for the exhibition:")
for plant, data in sorted_plants:
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {data['avg']:.2f}")