MAX_HIT_POINTS = 100
MAX_MANA_POINTS = 200


def cast_spell(heroes, name, needed_mp, spell_name):
    if heroes[name]['mana_points'] >= needed_mp:
        heroes[name]['mana_points'] -= needed_mp
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mana_points']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    return heroes


def take_damage(heroes, name, damage, attacker):
    heroes[name]['hit_points'] -= damage
    if heroes[name]['hit_points'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hit_points']} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del heroes[name]
    return heroes


def recharge_mana_points(heroes, name, amount):
    initial_mana_points = heroes[name]['mana_points']
    additional_mana_points = amount
    if initial_mana_points + additional_mana_points > MAX_MANA_POINTS:
        heroes[name]['mana_points'] = MAX_MANA_POINTS
        print(f"{name} recharged for {MAX_MANA_POINTS - initial_mana_points} MP!")
    else:
        heroes[name]['mana_points'] = initial_mana_points + additional_mana_points
        print(f"{name} recharged for {additional_mana_points} MP!")
    return heroes


def heal_hp(heroes, name, amount):
    initial_hit_points = heroes[name]['hit_points']
    additional_hit_points = amount
    if initial_hit_points + additional_hit_points > MAX_HIT_POINTS:
        heroes[name]['hit_points'] = MAX_HIT_POINTS
        print(f"{name} healed for {MAX_HIT_POINTS - initial_hit_points} HP!")
    else:
        heroes[name]['hit_points'] = initial_hit_points + additional_hit_points
        print(f"{name} healed for {additional_hit_points} HP!")
    return heroes


n = int(input())
heroes = {}

for _ in range(n):
    line = input()
    line = line.split()
    name, hit_points, mana_points = line[:]
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    heroes[name] = {'hit_points': hit_points, 'mana_points': mana_points}

line = input()

while not line == "End":
    line = line.split(" - ")
    action = line[0]
    if action == "CastSpell":
        name, needed_mp, spell_name = line[1:]
        needed_mp = int(needed_mp)
        heroes = cast_spell(heroes, name, needed_mp, spell_name)
    elif action == "TakeDamage":
        name, damage, attacker = line[1:]
        damage = int(damage)
        heroes = take_damage(heroes, name, damage, attacker)
    elif action == "Recharge":
        name, amount = line[1:]
        amount = int(amount)
        heroes = recharge_mana_points(heroes, name, amount)
    elif action == "Heal":
        name, amount = line[1:]
        amount = int(amount)
        heroes = heal_hp(heroes, name, amount)
    line = input()

sorted_party = sorted(heroes.items(), key=lambda x: (-x[1]['hit_points'], x[0]))

for name, points in sorted_party:
    print(f"{name}")
    print(f"  HP: {points['hit_points']}")
    print(f"  MP: {points['mana_points']}")
