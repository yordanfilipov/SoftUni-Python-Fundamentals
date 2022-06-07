def plunder_city(cities, city, people, gold):
    cities[city]['population'] -= people
    cities[city]['gold'] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
        del cities[city]
        print(f"{city} has been wiped off the map!")
    return cities


def prosper_city(cities, city, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return cities
    else:
        cities[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    return cities


cities = {}
command = input()

while not command == "Sail":
    command = command.split("||")
    city, population, gold = command[:]
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    command = input()

line = input()
while not line == "End":
    line = line.split("=>")
    action, city = line[:2]
    if action == "Plunder":
        people, gold = line[2:]
        people = int(people)
        gold = int(gold)
        cities = plunder_city(cities, city, people, gold)
    elif action == "Prosper":
        gold = line[2]
        gold = int(gold)
        cities = prosper_city(cities, city, gold)
    line = input()

if cities:
    sorted_cities = sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0]))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, data in sorted_cities:
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")