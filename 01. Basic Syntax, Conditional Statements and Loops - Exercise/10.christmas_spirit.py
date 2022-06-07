quantity = int(input())
days = int(input())

spirit = 0
budget = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += quantity * ornament_set
        spirit += 5
    if day % 3 == 0:
        budget += quantity * tree_skirt
        budget += quantity * tree_garlands
        spirit += 13
    if day % 5 == 0:
        budget += quantity * tree_lights
        spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights
    if day % 10 == 0 and day == days:
        spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')

